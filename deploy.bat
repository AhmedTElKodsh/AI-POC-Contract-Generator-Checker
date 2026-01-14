@echo off
echo ========================================
echo Streamlit Deployment Helper
echo ========================================
echo.

echo Step 1: Checking if git is initialized...
if not exist .git (
    echo Git not initialized. Initializing now...
    git init
    git branch -M main
) else (
    echo Git already initialized.
)

echo.
echo Step 2: Adding files to git...
git add .
git status

echo.
echo Step 3: Ready to commit and push!
echo.
echo Next steps:
echo 1. Run: git commit -m "Deploy Streamlit app"
echo 2. Create a GitHub repository at: https://github.com/new
echo 3. Run: git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
echo 4. Run: git push -u origin main
echo 5. Go to: https://share.streamlit.io
echo 6. Click "New app" and select your repository
echo.
echo Your app will be live at: https://YOUR_USERNAME-YOUR_REPO.streamlit.app
echo.
pause
