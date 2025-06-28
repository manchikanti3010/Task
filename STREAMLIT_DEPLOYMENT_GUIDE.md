# 🚀 Streamlit Cloud Deployment Guide

This guide will help you deploy your AI Research Assistant to Streamlit Cloud with proper API key configuration.

## Prerequisites

1. **GitHub Repository**: Your code must be on GitHub
2. **Google API Key**: Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
3. **Streamlit Account**: Sign up at [share.streamlit.io](https://share.streamlit.io)

## Step-by-Step Deployment

### Step 1: Push Your Code to GitHub

Make sure your code is pushed to GitHub (which you've already done):
```bash
git add .
git commit -m "Add Streamlit Cloud deployment support"
git push origin main
```

### Step 2: Deploy to Streamlit Cloud

1. **Go to Streamlit Cloud**: Visit [share.streamlit.io](https://share.streamlit.io)
2. **Sign in**: Use your GitHub account
3. **New App**: Click "New app"
4. **Repository**: Select your repository (`manchikanti3010/Task`)
5. **Branch**: Select `main`
6. **Main file path**: Enter `app.py`
7. **App URL**: Choose a custom URL (optional)
8. **Click "Deploy"**

### Step 3: Configure API Key (CRITICAL)

After deployment, you need to add your Google API key:

1. **Go to your deployed app**
2. **Click the hamburger menu** (☰) in the top right
3. **Select "Settings"**
4. **Scroll down to "Secrets"**
5. **Add your API key** in this format:

```toml
GOOGLE_API_KEY = "your_actual_api_key_here"
```

**Important**: Replace `your_actual_api_key_here` with your real Google API key.

### Step 4: Redeploy

1. **Save the secrets**
2. **Go back to your app**
3. **Click "Redeploy"** in the hamburger menu

## Troubleshooting

### Issue: "API key is not available"

**Cause**: The API key is not configured in Streamlit Cloud secrets.

**Solution**:
1. Go to your app's Settings → Secrets
2. Add the API key exactly as shown above
3. Redeploy the app

### Issue: "Module not found"

**Cause**: Missing dependencies in requirements.txt.

**Solution**: Make sure your `requirements.txt` includes:
```
streamlit
pypdf2
python-dotenv
google-generativeai
pandas
plotly
```

### Issue: "Permission denied"

**Cause**: Repository access issues.

**Solution**:
1. Make sure your repository is public
2. Or connect your GitHub account properly to Streamlit Cloud

## Security Best Practices

### ✅ Do's:
- Use Streamlit Cloud secrets for API keys
- Keep your repository public (for free tier)
- Use environment-specific API keys

### ❌ Don'ts:
- Never commit API keys to Git
- Don't hardcode secrets in your code
- Don't share your API keys publicly

## Testing Your Deployment

1. **Upload a document** (PDF or TXT)
2. **Try generating a summary**
3. **Test the Q&A feature**
4. **Check the analytics dashboard**

## Monitoring Your App

### Streamlit Cloud Dashboard:
- **Usage**: Monitor app usage and performance
- **Logs**: View application logs for debugging
- **Settings**: Manage app configuration

### API Usage:
- Monitor your Google API usage at [Google AI Studio](https://makersuite.google.com/app/apikey)
- Free tier includes generous limits

## Customization Options

### Environment Variables:
You can add more secrets in the same format:
```toml
GOOGLE_API_KEY = "your_api_key"
CUSTOM_SETTING = "value"
```

### App Configuration:
Edit `config.py` to customize:
- Model selection
- Text processing limits
- UI settings

## Performance Optimization

### For Better Performance:
1. **Use appropriate model**: Gemini 1.5 Flash is fast and efficient
2. **Limit text length**: Large documents are automatically chunked
3. **Cache results**: Session state preserves data during the session

### Cost Optimization:
1. **Monitor API usage**: Check your Google AI Studio dashboard
2. **Use free tier efficiently**: 15 requests per minute limit
3. **Implement rate limiting**: The app handles this automatically

## Advanced Features

### Custom Domain (Pro):
- Upgrade to Streamlit Cloud Pro
- Use your own domain name

### Team Collaboration:
- Invite team members
- Share app access
- Collaborate on development

## Support Resources

- **Streamlit Documentation**: [docs.streamlit.io](https://docs.streamlit.io)
- **Streamlit Community**: [discuss.streamlit.io](https://discuss.streamlit.io)
- **Google AI Studio**: [makersuite.google.com](https://makersuite.google.com)

## Common Commands

### Local Development:
```bash
streamlit run app.py
```

### Update Deployment:
```bash
git add .
git commit -m "Update message"
git push origin main
# Streamlit Cloud will auto-deploy
```

### Check App Status:
- Visit your app URL
- Check Streamlit Cloud dashboard
- Monitor GitHub repository

---

🎉 **Your AI Research Assistant is now live on Streamlit Cloud!**

**App URL**: `https://your-app-name.streamlit.app`

Share this URL with potential employers to showcase your work! 