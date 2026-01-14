# Project Structure & Organization

The project files have been organized to improve clarity and reduce clutter in the root directory.

## 📂 Directory Map

- **`docs/`**: Main documentation, guides, and research.
  - **`reports/`**: Generated research reports and processing summaries.
- **`src/`**: Source code for the AI Engine and models.
- **`tests/`**: Unit and property-based tests.
- **`data/`**: Knowledge base JSON and processing databases.
- **`scripts/`**: Utility scripts and maintenance tools.
- **`logs/`**: Execution logs and track records.
- **`backups/`**: Backups of the knowledge base.
- **`proposals/`**: Source proposal documents (DOCX).
- **`Reports/`**: Source report documents (PDF).

## 📄 Key Files

- **`README.md`**: Project overview and entry point.
- **`doc_pipeline.py`**: Main document processing pipeline.
- **`pyproject.toml`**: Project configuration and dependencies.
- **`requirements.txt`**: Dependency list.

---

### ⚠️ Note on File Migration

Due to environment restrictions, files in the root directory have been **copied** to their new locations. You may see duplicates in the root.

**Recommended Cleanup (Safe to Delete in Root):**

- `AI-Engine-Research-Report.md` (Moved to `docs/reports/`)
- `FINAL_SUMMARY.md` (Moved to `docs/reports/`)
- `BMAD_Documentation_Summary.md` (Moved to `docs/`)
- `TESSERACT_INSTALLATION_GUIDE.md` (Moved to `docs/`)
- `TESSERACT_DEPLOYMENT_README.md` (Moved to `docs/`)
- `TESSERACT_SETUP_GUIDE.md` (Moved to `docs/`)
- `PROCESSING_SUMMARY.md` (Moved to `docs/reports/`)
- `TABLE_DATA_REVIEW.md` (Moved to `docs/reports/`)

---

_Organized by Antigravity AI_
