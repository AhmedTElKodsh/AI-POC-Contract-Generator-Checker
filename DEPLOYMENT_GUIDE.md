# Streamlit Deployment Guide

## Deploy to Streamlit Community Cloud (FREE)

### Prerequisites

1. GitHub account
2. Your code pushed to a GitHub repository

### Step-by-Step Deployment

#### 1. Push Your Code to GitHub

If you haven't already, initialize git and push to GitHub:

```bash
git init
git add .
git commit -m "Initial commit - Streamlit app"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git push -u origin main
```

#### 2. Deploy on Streamlit Community Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with your GitHub account
3. Click "New app"
4. Fill in the details:
   - **Repository**: Select your GitHub repository
   - **Branch**: main
   - **Main file path**: app.py
5. Click "Deploy!"

Your app will be live at: `https://YOUR_USERNAME-YOUR_REPO_NAME.streamlit.app`

#### 3. Configuration Files

The following files have been created for deployment:

- `.streamlit/config.toml` - Streamlit configuration
- `streamlit_requirements.txt` - Python dependencies (lightweight version)
- `packages.txt` - System-level dependencies (if needed)

### Alternative Deployment Options

#### Option 2: Hugging Face Spaces (FREE)

1. Create account at [huggingface.co](https://huggingface.co)
2. Create new Space
3. Select "Streamlit" as SDK
4. Upload your files or connect GitHub repo
5. Your app will be at: `https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE_NAME`

#### Option 3: Railway.app (FREE tier available)

1. Sign up at [railway.app](https://railway.app)
2. Create new project from GitHub repo
3. Add environment variables if needed
4. Railway will auto-detect Streamlit and deploy

#### Option 4: Render.com (FREE tier available)

1. Sign up at [render.com](https://render.com)
2. Create new Web Service
3. Connect your GitHub repository
4. Set build command: `pip install -r streamlit_requirements.txt`
5. Set start command: `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`

### Important Notes

1. **Knowledge Base**: Make sure `knowledge_base.json` is included in your repo
2. **Templates**: Ensure the `templates/` folder is included
3. **File Size**: Keep your repo under 1GB for free hosting
4. **Dependencies**: Use `streamlit_requirements.txt` for faster deployment (only essential packages)

### Troubleshooting

**App won't start?**

- Check logs in Streamlit Cloud dashboard
- Verify all dependencies are in `streamlit_requirements.txt`
- Ensure `knowledge_base.json` exists

**Missing files?**

- Check that all required files are committed to git
- Verify paths in `app.py` are relative, not absolute

**Slow loading?**

- Reduce dependencies in `streamlit_requirements.txt`
- Consider lazy loading heavy libraries

### Sharing Your App

Once deployed, you can share the URL with anyone:

- No login required for viewers
- Works on mobile and desktop
- Can embed in websites using iframe

### Custom Domain (Optional)

Streamlit Community Cloud supports custom domains:

1. Go to app settings
2. Add custom domain
3. Update DNS records as instructed

---

**Need help?** Check [Streamlit docs](https://docs.streamlit.io/streamlit-community-cloud) or ask in [Streamlit forum](https://discuss.streamlit.io)
