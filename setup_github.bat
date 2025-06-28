@echo off
echo ========================================
echo GitHub Repository Setup Script
echo ========================================

echo.
echo Step 1: Initializing Git repository...
git init

echo.
echo Step 2: Adding all files to Git...
git add .

echo.
echo Step 3: Making initial commit...
git commit -m "Initial commit: AI Research Assistant Pro with Gemini API integration"

echo.
echo ========================================
echo Repository is ready for GitHub!
echo ========================================
echo.
echo Next steps:
echo 1. Go to https://github.com/new
echo 2. Create a new repository named "ai-research-assistant"
echo 3. DO NOT initialize with README (we already have one)
echo 4. Copy the repository URL
echo 5. Run the following commands:
echo.
echo git remote add origin https://github.com/YOUR_USERNAME/ai-research-assistant.git
echo git branch -M main
echo git push -u origin main
echo.
echo Replace YOUR_USERNAME with your actual GitHub username
echo ========================================
pause 