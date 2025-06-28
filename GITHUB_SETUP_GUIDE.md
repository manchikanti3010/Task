# 🚀 GitHub Setup Guide for AI Research Assistant

This guide will help you push your AI Research Assistant project to GitHub.

## Prerequisites

### 1. Install Git
- **Windows**: Download from https://git-scm.com/download/win
- **macOS**: Install via Homebrew: `brew install git`
- **Linux**: `sudo apt-get install git` (Ubuntu/Debian) or `sudo yum install git` (CentOS/RHEL)

### 2. Create GitHub Account
- Go to https://github.com
- Sign up for a free account
- Verify your email address

## Step-by-Step Process

### Step 1: Install Git (if not already installed)

**For Windows:**
1. Download Git from https://git-scm.com/download/win
2. Run the installer
3. Use default settings (recommended)
4. Restart your terminal/PowerShell

**Verify installation:**
```bash
git --version
```

### Step 2: Configure Git (First time only)

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Step 3: Initialize Local Repository

Run one of these scripts in your project directory:

**PowerShell:**
```powershell
.\setup_github.ps1
```

**Command Prompt:**
```cmd
setup_github.bat
```

**Or manually:**
```bash
git init
git add .
git commit -m "Initial commit: AI Research Assistant Pro with Gemini API integration"
```

### Step 4: Create GitHub Repository

1. Go to https://github.com/new
2. Repository name: `ai-research-assistant`
3. Description: `Professional AI Research Assistant powered by Google Gemini API`
4. **Important**: Do NOT check "Add a README file" (we already have one)
5. Click "Create repository"

### Step 5: Connect and Push to GitHub

Replace `YOUR_USERNAME` with your actual GitHub username:

```bash
git remote add origin https://github.com/YOUR_USERNAME/ai-research-assistant.git
git branch -M main
git push -u origin main
```

### Step 6: Verify Upload

1. Go to your GitHub repository: `https://github.com/YOUR_USERNAME/ai-research-assistant`
2. You should see all your files uploaded
3. The README.md should display nicely on the main page

## Authentication Options

### Option 1: Personal Access Token (Recommended)
1. Go to GitHub Settings → Developer settings → Personal access tokens
2. Generate new token (classic)
3. Select scopes: `repo`, `workflow`
4. Copy the token and use it as your password when prompted

### Option 2: GitHub CLI
```bash
# Install GitHub CLI
# Windows: winget install GitHub.cli
# macOS: brew install gh
# Linux: sudo apt install gh

gh auth login
gh repo create ai-research-assistant --public --source=. --remote=origin --push
```

### Option 3: SSH Keys
1. Generate SSH key: `ssh-keygen -t ed25519 -C "your.email@example.com"`
2. Add to GitHub: Settings → SSH and GPG keys
3. Use SSH URL: `git@github.com:YOUR_USERNAME/ai-research-assistant.git`

## Repository Structure

Your GitHub repository should contain:
```
ai-research-assistant/
├── app.py                 # Main Streamlit application
├── utils.py              # Core utility functions
├── config.py             # Configuration settings
├── test_setup.py         # Setup validation script
├── requirements.txt      # Python dependencies
├── README.md            # Project documentation
├── .gitignore           # Git ignore rules
├── setup_github.bat     # Windows setup script
├── setup_github.ps1     # PowerShell setup script
└── GITHUB_SETUP_GUIDE.md # This guide
```

## Troubleshooting

### Common Issues

**1. "git is not recognized"**
- Git is not installed or not in PATH
- Solution: Install Git and restart terminal

**2. "Authentication failed"**
- Use Personal Access Token instead of password
- Or set up SSH keys

**3. "Repository already exists"**
- Delete the repository on GitHub first
- Or use a different name

**4. "Permission denied"**
- Check if you have write access to the repository
- Ensure you're using the correct GitHub account

### Useful Commands

```bash
# Check Git status
git status

# Check remote repository
git remote -v

# View commit history
git log --oneline

# Update repository
git add .
git commit -m "Update message"
git push

# Clone repository (for others)
git clone https://github.com/YOUR_USERNAME/ai-research-assistant.git
```

## Next Steps

After successfully uploading to GitHub:

1. **Add a License**: Go to repository settings → General → License
2. **Set up GitHub Pages**: For project documentation
3. **Add Topics**: Help others find your project
4. **Create Issues**: For feature requests and bug reports
5. **Set up Actions**: For automated testing and deployment

## Professional Tips

1. **Keep .env file private**: It's already in .gitignore
2. **Update README**: Add screenshots and demo links
3. **Add badges**: Build status, version, etc.
4. **Create releases**: Tag important versions
5. **Respond to issues**: Engage with the community

## Deployment Options

Once on GitHub, you can deploy your app:

1. **Streamlit Cloud**: Free hosting for Streamlit apps
2. **Heroku**: Cloud platform with free tier
3. **Railway**: Modern deployment platform
4. **Vercel**: Fast deployment with serverless functions

---

🎉 **Congratulations!** Your AI Research Assistant is now on GitHub and ready to impress potential employers! 