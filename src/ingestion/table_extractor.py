"""Table extraction from documents."""

import re
from typing import Any, Optional

from src.models.documents import TableData


class TableExtractor:
    """Extract and parse tables from document content."""

    def __init__(self):
        """Initialize the table extractor."""
        pass

    def extract_from_markdown(self, markdown_text: str) -> list[TableData]:
        """
        Extract tables from markdown-formatted text.

        Args:
            markdown_text: Markdown text containing tables

        Returns:
            List of TableData objects
        """
        tables = []
        lines = markdown_text.split("\n")
        i = 0

        while i < len(lines):
            line = lines[i].strip()

            # Check for markdown table start (line with |)
            if "|" in line and self._is_table_row(line):
                table_lines = [line]
                i += 1

                # Collect all table rows
                while i < len(lines):
                    next_line = lines[i].strip()
                    if "|" in next_line and (
                        self._is_table_row(next_line) or self._is_separator_row(next_line)
                    ):
                        table_lines.append(next_line)
                        i += 1
                    else:
                        break

                # Parse the collected table
                table = self._parse_markdown_table(table_lines)
                if table:
                    tables.append(table)
            else:
                i += 1

        return tables

    def _is_table_row(self, line: str) -> bool:
        """Check if a line is a table row."""
        return line.startswith("|") or line.endswith("|")

    def _is_separator_row(self, line: str) -> bool:
        """Check if a line is a table separator row (|---|---|)."""
        return bool(re.match(r"^\|?[\s\-:]+\|[\s\-:|]+\|?$", line))

    def _parse_markdown_table(self, lines: list[str]) -> Optional[TableData]:
        """Parse markdown table lines into TableData."""
        if len(lines) < 2:
            return None

        # Filter out separator rows
        data_lines = [line for line in lines if not self._is_separator_row(line)]

        if not data_lines:
            return None

        # Parse header (first row)
        headers = self._parse_row(data_lines[0])

        # Parse data rows
        rows = []
        for line in data_lines[1:]:
            row = self._parse_row(line)
            if row:
                # Pad or trim row to match header length
                while len(row) < len(headers):
                    row.append("")
                rows.append(row[: len(headers)])

        return TableData(headers=headers, rows=rows, caption=None, page_number=None)

    def _parse_row(self, line: str) -> list[str]:
        """Parse a single table row."""
        # Remove leading/trailing pipes and split
        line = line.strip()
        if line.startswith("|"):
            line = line[1:]
        if line.endswith("|"):
            line = line[:-1]

        cells = [cell.strip() for cell in line.split("|")]
        return cells

    def extract_boq_table(self, table: TableData) -> Optional[dict[str, Any]]:
        """
        Identify and parse a Bill of Quantities (BOQ) table.

        Args:
            table: TableData to analyze

        Returns:
            Parsed BOQ data or None if not a BOQ table
        """
        # Common BOQ header patterns
        boq_keywords = [
            "item",
            "description",
            "unit",
            "quantity",
            "rate",
            "amount",
            "total",
            "بند",  # Arabic: item
            "الوصف",  # Arabic: description
            "الوحدة",  # Arabic: unit
            "الكمية",  # Arabic: quantity
        ]

        # Check if headers match BOQ pattern
        header_lower = [h.lower() for h in table.headers]
        matches = sum(1 for kw in boq_keywords if any(kw in h for h in header_lower))

        if matches < 3:
            return None

        # Parse BOQ items
        items = []
        for row in table.rows:
            item = self._parse_boq_row(table.headers, row)
            if item:
                items.append(item)

        return {"type": "boq", "headers": table.headers, "items": items}

    def _parse_boq_row(
        self, headers: list[str], row: list[str]
    ) -> Optional[dict[str, Any]]:
        """Parse a single BOQ row."""
        if len(row) != len(headers):
            return None

        item = {}
        header_lower = [h.lower() for h in headers]

        for i, (header, value) in enumerate(zip(header_lower, row)):
            if "item" in header or "no" in header or "بند" in header:
                item["item_number"] = value
            elif "desc" in header or "الوصف" in header:
                item["description"] = value
            elif "unit" in header or "الوحدة" in header:
                item["unit"] = value
            elif "qty" in header or "quantity" in header or "الكمية" in header:
                item["quantity"] = self._parse_number(value)
            elif "rate" in header or "price" in header or "السعر" in header:
                item["unit_rate"] = self._parse_number(value)
            elif "amount" in header or "total" in header or "المبلغ" in header:
                item["total"] = self._parse_number(value)

        return item if item else None

    def _parse_number(self, value: str) -> Optional[float]:
        """Parse a numeric value from string."""
        if not value:
            return None

        # Remove currency symbols and commas
        cleaned = re.sub(r"[^\d.\-]", "", value.replace(",", ""))

        try:
            return float(cleaned) if cleaned else None
        except ValueError:
            return None
