Write-Host "========================================" -ForegroundColor Green
Write-Host "GitHub Repository Setup Script" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green

Write-Host ""
Write-Host "Step 1: Initializing Git repository..." -ForegroundColor Yellow
git init

Write-Host ""
Write-Host "Step 2: Adding all files to Git..." -ForegroundColor Yellow
git add .

Write-Host ""
Write-Host "Step 3: Making initial commit..." -ForegroundColor Yellow
git commit -m "Initial commit: AI Research Assistant Pro with Gemini API integration"

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "Repository is ready for GitHub!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "1. Go to https://github.com/new" -ForegroundColor White
Write-Host "2. Create a new repository named 'ai-research-assistant'" -ForegroundColor White
Write-Host "3. DO NOT initialize with README (we already have one)" -ForegroundColor White
Write-Host "4. Copy the repository URL" -ForegroundColor White
Write-Host "5. Run the following commands:" -ForegroundColor White
Write-Host ""
Write-Host "git remote add origin https://github.com/YOUR_USERNAME/ai-research-assistant.git" -ForegroundColor Magenta
Write-Host "git branch -M main" -ForegroundColor Magenta
Write-Host "git push -u origin main" -ForegroundColor Magenta
Write-Host ""
Write-Host "Replace YOUR_USERNAME with your actual GitHub username" -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Green

Read-Host "Press Enter to continue" 