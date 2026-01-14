const fs = require('fs');
const path = require('path');

const logFile = 'organize_log.txt';
function log(msg) {
    console.log(msg);
    fs.appendFileSync(logFile, msg + '\n');
}

fs.writeFileSync(logFile, 'Starting organization...\n');

const dirs = [
    'docs/reports',
    'scripts',
    'data',
    'backups',
    'logs'
];

dirs.forEach(dir => {
    if (!fs.existsSync(dir)) {
        fs.mkdirSync(dir, { recursive: true });
        log(`Created directory: ${dir}`);
    }
});

const moves = [
    { from: 'AI-Engine-Research-Report.md', to: 'docs/reports/AI-Engine-Research-Report.md' },
    { from: 'BMAD_Documentation_Summary.md', to: 'docs/BMAD_Documentation_Summary.md' },
    { from: 'BMAD_IMPLEMENTATION_REPORT.md', to: 'docs/reports/BMAD_IMPLEMENTATION_REPORT.md' },
    { from: 'BMAD_TEST_REVIEW_REPORT.md', to: 'docs/reports/BMAD_TEST_REVIEW_REPORT.md' },
    { from: 'FINAL_SUMMARY.md', to: 'docs/reports/FINAL_SUMMARY.md' },
    { from: 'IMPLEMENTATION_REPORT.md', to: 'docs/reports/IMPLEMENTATION_REPORT.md' },
    { from: 'KNOWLEDGE_BASE_DOUBLE_REVIEW_REPORT.md', to: 'docs/reports/KNOWLEDGE_BASE_DOUBLE_REVIEW_REPORT.md' },
    { from: 'PROCESSING_SUMMARY.md', to: 'docs/reports/PROCESSING_SUMMARY.md' },
    { from: 'RESEARCH_STORIES_COMPLETION_REPORT.md', to: 'docs/reports/RESEARCH_STORIES_COMPLETION_REPORT.md' },
    { from: 'TABLE_DATA_REVIEW.md', to: 'docs/reports/TABLE_DATA_REVIEW.md' },
    { from: 'TESSERACT_DEPLOYMENT_README.md', to: 'docs/TESSERACT_DEPLOYMENT_README.md' },
    { from: 'TESSERACT_INSTALLATION_GUIDE.md', to: 'docs/TESSERACT_INSTALLATION_GUIDE.md' },
    { from: 'TESSERACT_SETUP_GUIDE.md', to: 'docs/TESSERACT_SETUP_GUIDE.md' },
    { from: 'advanced_ai_api_docs.md', to: 'docs/advanced_ai_api_docs.md' },
    { from: 'advanced_ai_glossaries.md', to: 'docs/advanced_ai_glossaries.md' },
    { from: 'advanced_ai_integration_guides.md', to: 'docs/advanced_ai_integration_guides.md' },
    { from: 'advanced_ai_references.md', to: 'docs/advanced_ai_references.md' },
    { from: 'advanced_ai_research_stories.md', to: 'docs/advanced_ai_research_stories.md' },
    { from: 'completion_report.md', to: 'docs/reports/completion_report.md' },
    { from: 'extract_docs.py', to: 'scripts/extract_docs.py' },
    { from: 'retry_extract.py', to: 'scripts/retry_extract.py' },
    { from: 'remove_uv.bat', to: 'scripts/remove_uv.bat' },
    { from: 'remove_uv.ps1', to: 'scripts/remove_uv.ps1' },
    { from: 'fix.js', to: 'scripts/fix.js' },
    { from: 'knowledge_base.json', to: 'data/knowledge_base.json' },
    { from: 'processing_tracker.db', to: 'data/processing_tracker.db' },
    { from: 'knowledge_base.json.backup', to: 'backups/knowledge_base.json.backup' },
    { from: 'knowledge_base.json.backup-before-pdfplumber', to: 'backups/knowledge_base.json.backup-before-pdfplumber' },
    { from: 'document_processing.log', to: 'logs/document_processing.log' },
    { from: 'output.log', to: 'logs/output.log' },
    { from: 'test_output.txt', to: 'logs/test_output.txt' },
    { from: 'test_fixes.py', to: 'tests/test_fixes.py' },
    { from: 'test_fixes_no_main.py', to: 'tests/test_fixes_no_main.py' }
];

moves.forEach(m => {
    if (fs.existsSync(m.from)) {
        try {
            // Ensure target directory exists
            const targetDir = path.dirname(m.to);
            if (!fs.existsSync(targetDir)) {
                fs.mkdirSync(targetDir, { recursive: true });
            }
            fs.renameSync(m.from, m.to);
            log(`Moved: ${m.from} -> ${m.to}`);
        } catch (e) {
            log(`Error moving ${m.from}: ${e.message}`);
        }
    } else {
        log(`Skipped (not found): ${m.from}`);
    }
});

log('Organization complete.');
