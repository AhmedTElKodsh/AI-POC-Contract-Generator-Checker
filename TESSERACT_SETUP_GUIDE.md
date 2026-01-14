# TESSERACT OCR INSTALLATION & CONFIGURATION

## Current Status: OCR Not Available

Tesseract OCR is not currently detected on your system. Follow these steps to install and configure it properly.

---

## 🔧 INSTALLATION STEPS

### Step 1: Download Tesseract OCR
1. Visit: https://github.com/UB-Mannheim/tesseract/wiki
2. Download: `tesseract-ocr-w64-setup-5.x.x.exe` (64-bit Windows installer)
3. Save to your Downloads folder

### Step 2: Run Installer
1. **Double-click** the downloaded `.exe` file
2. **Installation Options:**
   - ✅ **Install location**: `C:\Program Files\Tesseract-OCR`
   - ✅ **Language packs**: Select **English** AND **Arabic**
   - ✅ **Additional options**: Check **"Add Tesseract to PATH"**
3. Click **Install** and wait for completion

### Step 3: Verify Installation
Open a **NEW Command Prompt** (restart terminal) and run:
```cmd
tesseract --version
tesseract --list-langs
```

**Expected Output:**
```
tesseract v5.x.x
List of available languages (2):
ara
eng
```

### Step 4: Test Python Integration
```bash
python -c "import pytesseract; print('Tesseract version:', pytesseract.get_tesseract_version())"
```

---

## 🔍 TROUBLESHOOTING

### If "tesseract is not recognized"
1. **Restart your terminal/command prompt**
2. **Check if added to PATH during installation**
3. **Manual PATH addition:**
   - Right-click "This PC" → "Properties" → "Advanced system settings"
   - Click "Environment Variables"
   - Under "System variables", find "Path" and click "Edit"
   - Click "New" and add: `C:\Program Files\Tesseract-OCR`
   - Click OK on all dialogs
   - **Restart terminal**

### If Language Packs Missing
Re-run installer and ensure Arabic (`ara`) is selected.

### If Python Still Can't Find It
Set explicit path in code:
```python
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

---

## 📋 POST-INSTALLATION TESTING

Once installed, run these commands to test:

```bash
# 1. Check OCR availability
python doc_pipeline.py --health-check

# 2. Process documents (should now extract OCR content)
python doc_pipeline.py

# 3. Verify OCR document was processed
python -c "
import json
with open('knowledge_base.json', 'r', encoding='utf-8') as f:
    kb = json.load(f)
docs = [k for k in kb.keys() if not k.startswith('knowledge_base')]
ocr_docs = [k for k in docs if 'OCR' in str(kb[k])]
print(f'Documents: {len(docs)}')
print(f'OCR processed: {len(ocr_docs)}')
if ocr_docs:
    print('OCR document found - extraction successful!')
"
```

---

## 🎯 EXPECTED RESULTS AFTER INSTALLATION

### Before Installation
```
OCR Status: NOT AVAILABLE
Documents with OCR content: 0
```

### After Installation
```
OCR Status: AVAILABLE (Tesseract v5.x.x)
Documents with OCR content: 1
OCR document found - extraction successful!
```

---

## 📞 SUPPORT

If you encounter issues:
1. Verify installation location: `C:\Program Files\Tesseract-OCR`
2. Check PATH includes Tesseract directory
3. Restart terminal/command prompt
4. Run installer again if needed

**Once Tesseract is properly installed and configured, the scanned PDF will be automatically processed with OCR during the next document pipeline run.**
