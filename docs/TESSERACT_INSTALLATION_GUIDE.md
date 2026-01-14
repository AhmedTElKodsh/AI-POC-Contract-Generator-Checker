# Tesseract OCR Installation Guide

## Purpose

This guide provides step-by-step instructions to install Tesseract OCR for processing scanned PDFs in the document processing pipeline.

---

## Why Tesseract OCR is Needed

Currently, one PDF file in the Reports folder cannot be fully processed:

- `تقرير دراسة السيول لطريق منفلوط الداخلة- شركة أرابكو (STA.160+000-STA.200+000).pdf`

This PDF appears to be a **scanned document** (image-based) and requires OCR to extract text content.

---

## Installation Instructions

### Option 1: Windows (Recommended)

#### Step 1: Download Tesseract Installer

Visit the official Tesseract GitHub releases page:
https://github.com/UB-Mannheim/tesseract/wiki

Download the latest Windows installer:

- File: `tesseract-ocr-w64-setup-5.x.x.exe` (for 64-bit Windows)
- Alternative: Direct download from https://github.com/UB-Mannheim/tesseract/releases

#### Step 2: Run Installer

1. Double-click the downloaded `.exe` file
2. Choose installation directory (recommended: `C:\Program Files\Tesseract-OCR`)
3. Select additional language data:
   - ✅ English
   - ✅ Arabic
   - ✅ Other languages as needed
4. Click "Install"
5. When prompted, select:
   - ✅ Add Tesseract to system PATH
   - ✅ Create desktop shortcut

#### Step 3: Verify Installation

Open a new Command Prompt or PowerShell window and run:

```cmd
tesseract --version
```

Expected output:

```
tesseract 5.x.x
 leptonica-1.xx.xx
  libgif 5.x.x : libjpeg 8.d : libpng 1.x.x : libtiff 4.x.x
 zlib 1.x.x : libwebp 1.x.x
```

#### Step 4: Install Language Packs (if not already)

If you need additional languages after installation:

1. Download language data files from:
   https://github.com/tesseract-ocr/tessdata/raw/main/eng.traineddata
   https://github.com/tesseract-ocr/tessdata/raw/main/ara.traineddata

2. Copy `.traineddata` files to:
   ```
   C:\Program Files\Tesseract-OCR\tessdata\
   ```

#### Step 5: Update PATH (if needed)

If Tesseract is not found in PATH:

1. Right-click "This PC" → "Properties" → "Advanced system settings"
2. Click "Environment Variables"
3. Under "System variables", find "Path" and click "Edit"
4. Click "New" and add:
   ```
   C:\Program Files\Tesseract-OCR
   ```
5. Click "OK" on all dialog boxes
6. Restart your terminal/IDE

---

### Option 2: Linux (Ubuntu/Debian)

```bash
# Update package list
sudo apt update

# Install Tesseract with English and Arabic language packs
sudo apt install -y tesseract-ocr tesseract-ocr-eng tesseract-ocr-ara

# Verify installation
tesseract --version

# List installed languages
tesseract --list-langs
```

Expected output includes:

```
eng
ara
```

---

### Option 3: macOS (Homebrew)

```bash
# Install Tesseract
brew install tesseract

# Install language packs
brew install tesseract-lang

# Verify installation
tesseract --version

# List installed languages
tesseract --list-langs
```

---

## Configuration for Python

The `doc_pipeline.py` script uses `pytesseract` (Python wrapper). After installing Tesseract:

### Verify Python can find Tesseract

```bash
python -c "import pytesseract; print(pytesseract.get_tesseract_version())"
```

Expected output:

```
tesseract 5.x.x
```

### If Python cannot find Tesseract

Add this to your script before running OCR:

```python
import pytesseract

# Set Tesseract path explicitly (Windows example)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# macOS/Linux example (usually not needed)
# pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
```

---

## Re-processing Documents After Installation

### Step 1: Verify OCR is Enabled

Run the pipeline:

```bash
python doc_pipeline.py
```

You should see in the logs:

```
Tesseract OCR v5.x.x detected and enabled
OCR Enabled: True
```

### Step 2: Process All Documents

The pipeline will automatically:

1. Detect scanned PDFs
2. Use OCR to extract text
3. Include OCR results in knowledge_base.json

### Step 3: Verify Results

Check the processed document:

```bash
python -c "import json; kb = json.load(open('knowledge_base.json', 'r', encoding='utf-8')); doc = kb.get('reports_تقرير دراسة السيول لطريق منفلوط الداخلة- شركة أرابكو'); print('OCR Extracted:', 'OCR' in str(doc.get('segments', {})))"
```

---

## Troubleshooting

### Issue: "tesseract is not installed or it's not in your PATH"

**Solutions:**

1. Re-run Tesseract installer and ensure "Add to PATH" is checked
2. Manually add installation directory to system PATH
3. Set explicit path in Python script (see Configuration section above)

### Issue: "Failed loading language 'ara'"

**Solutions:**

1. Verify language files exist in `tessdata` folder
2. Re-download `ara.traineddata` from GitHub
3. Place in correct directory:
   - Windows: `C:\Program Files\Tesseract-OCR\tessdata\`
   - Linux: `/usr/share/tesseract-ocr/4.00/tessdata/`
   - macOS: `/usr/local/share/tessdata/`

### Issue: OCR quality is poor

**Solutions:**

1. Use higher resolution source documents
2. Pre-process images (increase contrast, remove noise)
3. Try different OCR modes in the script
4. Consider using more specialized OCR tools for Arabic:
   - Google Cloud Vision API
   - Amazon Textract
   - Microsoft Azure Computer Vision
   - ABBYY FineReader

---

## Performance Considerations

### OCR Processing Time

- **Typical document**: 5-10 seconds per page
- **Large documents (100+ pages)**: 5-15 minutes

### Resource Usage

- **CPU**: Heavy during processing
- **Memory**: 100-500 MB per document
- **Disk**: Language packs are 10-20 MB each

### Recommendations

1. Process documents sequentially (not in parallel)
2. Monitor system resources during OCR
3. Consider using a queue system for batch processing

---

## Alternatives to Tesseract

If Tesseract OCR doesn't meet your needs:

### Commercial Options

- **ABBYY FineReader**: Excellent for Arabic, but paid
- **Adobe Acrobat Pro**: Built-in OCR, subscription-based
- **Readiris**: Good multilingual support, paid

### Cloud-Based Options

- **Google Cloud Vision API**: Excellent OCR, pay-per-use
- **Amazon Textract**: Good for documents with tables
- **Microsoft Azure OCR**: Competitive pricing, good quality
- **OCR.space**: Free tier available, REST API

### Python Libraries with Cloud OCR

```python
# Google Cloud Vision example
from google.cloud import vision
client = vision.ImageAnnotatorClient()
response = client.document_text_detection(image=image)

# Amazon Textract example
import boto3
textract = boto3.client('textract')
response = textract.detect_document_text(Document={'Bytes': image_bytes})
```

---

## After Installation

1. ✅ Re-run `python doc_pipeline.py`
2. ✅ Check logs for "OCR enabled" message
3. ✅ Verify scanned PDF is now processed
4. ✅ Review OCR-extracted content in knowledge_base.json
5. ✅ Test accuracy and adjust if needed

---

## Support Resources

- **Tesseract Documentation**: https://tesseract-ocr.github.io/
- **Tesseract GitHub**: https://github.com/tesseract-ocr/tesseract
- **Tessdata (Language Packs)**: https://github.com/tesseract-ocr/tessdata
- **pytesseract Documentation**: https://github.com/madmaze/pytesseract

---

## Summary

| Item                        | Status     |
| --------------------------- | ---------- |
| Tesseract OCR Installation  | ⏳ Pending |
| Language Packs (Eng+Arabic) | ⏳ Pending |
| Python Configuration        | ⏳ Pending |
| Document Re-processing      | ⏳ Pending |

**Next Step**: Install Tesseract OCR using Option 1 (Windows) or your preferred method, then re-run the document processing pipeline.
