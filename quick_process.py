#!/usr/bin/env python
# Quick processing script - processes all files except problematic scanned PDF

import sys
import pathlib
import json

# Add current directory to path
sys.path.insert(0, str(pathlib.Path(__file__).parent))

import doc_pipeline

# Skip problematic scanned PDF
skip_file = "تقرير دراسة السيول لطريق منفلوط الداخلة- شركة أرابكو (STA.160+000-STA.200+000).pdf"

# Base folders
base_dir = pathlib.Path(__file__).parent.resolve()
proposals_folder = base_dir / "proposals"
reports_folder = base_dir / "Reports"

base_folders = {"proposals": str(proposals_folder), "reports": str(reports_folder)}

print("=" * 60)
print("QUICK PROCESSING - Skip problematic scanned PDF")
print("=" * 60)

# Clear duplicate tracker to allow reprocessing
print("\nClearing duplicate tracker...")
import sqlite3

db_path = "processing_tracker.db"
conn = sqlite3.connect(db_path)
conn.execute("DELETE FROM processed_files")
conn.commit()
conn.close()
print("[OK] Tracker cleared")

# Process all documents
print("\nProcessing documents...")
result = doc_pipeline.process_all_documents(
    base_folders,
    force_reprocess=True,  # Force reprocessing
    existing_kb=None,
)

# Skip the problematic scanned PDF manually
for doc_id in list(result.keys()):
    doc_data = result[doc_id]
    if skip_file in doc_data.get("file_path", ""):
        print(f"[SKIP] Skipping problematic file: {pathlib.Path(doc_data['file_path']).name}")
        del result[doc_id]

# Save knowledge base
kb_path = base_dir / "knowledge_base.json"
doc_pipeline.atomic_save_json(result, kb_path)

processed_count = len([k for k in result.keys() if not k.startswith("knowledge_base")])
print(f"\n[OK] Processed {processed_count} documents")
print(f"[OK] Knowledge base saved to: {kb_path}")
print("=" * 60)
