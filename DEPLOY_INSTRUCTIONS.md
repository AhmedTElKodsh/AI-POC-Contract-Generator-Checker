# 🚀 Deploy Your Streamlit App Online

## Quick Start - Streamlit Community Cloud (FREE & EASIEST)

### Step 1: Push to GitHub

```bash
# Initialize git (if not already done)
git init
git add .
git commit -m "Initial commit - Streamlit app"
git branch -M main

# Create a new repository on GitHub, then:
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git push -u origin main
```

### Step 2: Deploy on Streamlit Cloud

1. **Go to**: [share.streamlit.io](https://share.streamlit.io)
2. **Sign in** with your GitHub account
3. **Click** "New app"
4. **Configure**:
   - Repository: `YOUR_USERNAME/YOUR_REPO_NAME`
   - Branch: `main`
   - Main file path: `app.py`
   - Python version: 3.11
5. **Click** "Deploy!"

**Your app will be live at**: `https://YOUR_USERNAME-YOUR_REPO_NAME.streamlit.app`

### Step 3: Share the Link

Once deployed, share your app URL with anyone - no login required!

---

## Alternative Options

### Option 2: Hugging Face Spaces (FREE)

1. Create account at [huggingface.co](https://huggingface.co)
2. Create new Space → Select "Streamlit" SDK
3. Upload files or connect GitHub
4. Live at: `https://huggingface.co/spaces/YOUR_USERNAME/SPACE_NAME`

### Option 3: Railway.app (FREE tier)

1. Sign up at [railway.app](https://railway.app)
2. New project → Deploy from GitHub
3. Auto-detects Streamlit
4. Live in minutes

---

## Files Created for Deployment

✅ `.streamlit/config.toml` - App configuration
✅ `streamlit_requirements.txt` - Python dependencies
✅ `packages.txt` - System dependencies
✅ `.gitignore` - Files to exclude from git

---

## Important Notes

- **Knowledge Base**: Ensure `knowledge_base.json` is in your repo
- **Templates**: Include the `templates/` folder
- **File Size**: Keep repo under 1GB for free hosting
- **Dependencies**: Use `streamlit_requirements.txt` (not `requirements.txt`) for faster deployment

---

## Troubleshooting

**App won't start?**

- Check deployment logs in Streamlit Cloud dashboard
- Verify all files are committed to git
- Ensure paths in `app.py` are relative

**Missing dependencies?**

- Add them to `streamlit_requirements.txt`
- Redeploy from Streamlit Cloud dashboard

---

## Need Help?

- [Streamlit Docs](https://docs.streamlit.io/streamlit-community-cloud)
- [Streamlit Forum](https://discuss.streamlit.io)
