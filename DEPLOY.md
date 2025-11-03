# Deploy to Render.com

This **Flask** application is fully ready for deployment on Render.com. Follow these steps to deploy your Legal Assistant RAG application.

## 🚀 Quick Deployment Steps

### 1. Push to GitHub

First, make sure your code is on GitHub:

```bash
git init
git add .
git commit -m "Ready for Render.com deployment - Clean Flask application"
git branch -M main
git remote add origin https://github.com/yourusername/legal-assistant.git
git push -u origin main
```

### 2. Deploy on Render.com

1. **Sign up/Login** to [Render.com](https://render.com)
2. **Click "New +"** → **"Web Service"**
3. **Connect your GitHub repository**
4. **Configure your service:**
   - **Name**: `legal-assistant` (or your preferred name)
   - **Region**: Choose nearest to your users
   - **Branch**: `main`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`

### 3. Set Environment Variables

In your Render dashboard, add these environment variables:

#### Required Environment Variables:
```
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
SECRET_KEY=your_secret_key_here_32_characters_long
```

#### Optional Environment Variables:
```
PYTHON_VERSION=3.11.0
PORT=10000
```

### 4. Deploy!

Click **"Create Web Service"** and Render will automatically deploy your Flask application.

## 📁 Clean Flask Project Structure

```
legal-assistant/
├── app.py                 # Main Flask application (16.7KB)
├── templates/
│   └── index.html        # Frontend template (41KB, 1,266 lines)
├── requirements.txt      # Python dependencies (Flask, requests, etc.)
├── .env.example          # Environment variables template
├── Procfile              # Render process definition
├── runtime.txt           # Python 3.11.0 specification
├── render.yaml           # Render service configuration
├── DEPLOY.md             # This deployment guide
├── README.md             # Project documentation
├── start.sh              # Local development script
└── .gitignore            # Python/Flask git ignore rules
```

### ✅ No Node.js Dependencies
- **Pure Python/Flask application**
- **No package.json, node_modules, or JavaScript build tools**
- **Single command deployment: `pip install -r requirements.txt`**
- **Minimal dependencies for fast deployment**

## 📋 Pre-Deployment Checklist

### ✅ Required Flask Files
- [x] `app.py` - Main Flask application
- [x] `requirements.txt` - Python dependencies
- [x] `templates/index.html` - Frontend template
- [x] `render.yaml` - Render configuration (optional)
- [x] `Procfile` - Process definition
- [x] `runtime.txt` - Python version specification
- [x] `.gitignore` - Git ignore file

### ✅ API Keys Needed
1. **Groq API Key**: Get from [https://groq.com](https://groq.com)
2. **Tavily API Key**: Get from [https://tavily.com](https://tavily.com)

### ✅ Production Features
- [x] Health check endpoint (`/health`)
- [x] Production-ready Flask configuration
- [x] Environment variable handling
- [x] Error handling and logging
- [x] Security headers
- [x] HTTPS-only cookies in production
- [x] Proper session management

## 🔧 Configuration Details

### Environment Variables Explained

| Variable | Required | Description | Example |
|----------|----------|-------------|---------|
| `GROQ_API_KEY` | ✅ | Groq API key for LLM | `gsk_...` |
| `TAVILY_API_KEY` | ✅ | Tavily API key for search | `tvly-...` |
| `SECRET_KEY` | ✅ | Flask session secret key | `32_character_long_string` |
| `PORT` | ❌ | Port number (Render sets this) | `10000` |
| `PYTHON_VERSION` | ❌ | Python version | `3.11.0` |

### Render.com Features Used

- **Free Tier**: Available for hobby projects
- **Auto-Deploy**: Automatically deploys on git push
- **HTTPS**: Automatic SSL certificate
- **Health Checks**: Built-in health monitoring
- **Environment Variables**: Secure configuration
- **Custom Domains**: Available on paid plans

## 🌐 Accessing Your App

After deployment, your app will be available at:
`https://your-service-name.onrender.com`

## 🔍 Troubleshooting

### Common Issues and Solutions

#### 1. Build Fails
```bash
# Check your requirements.txt
pip install -r requirements.txt
```

#### 2. Environment Variables Not Working
- Ensure variables are set in Render dashboard
- Check variable names match exactly
- Restart your service after adding variables

#### 3. API Errors
- Verify API keys are correct
- Check API key permissions
- Monitor logs in Render dashboard

#### 4. Session Issues
- Sessions work automatically with cookies
- No filesystem required (uses signed cookies)
- Clear browser cookies if needed

#### 5. Streaming Not Working
- App falls back to regular responses
- Check browser console for errors
- Ensure WebSocket connections are allowed

## 📊 Monitoring

### Render Dashboard Features
- **Metrics**: CPU, memory, response times
- **Logs**: Real-time application logs
- **Alerts**: Email notifications for issues
- **Deployments**: Deployment history and rollback

### Health Check
Visit `/health` to check application status:
```json
{
  "status": "healthy",
  "timestamp": "2024-01-01T12:00:00.000Z",
  "version": "1.0.0"
}
```

## 🔒 Security Considerations

### Implemented Security Features
- HTTPS-only in production
- Secure cookies (HttpOnly, Secure, SameSite)
- Security headers (X-Frame-Options, CSP)
- Environment variable protection
- Input validation and sanitization

### Recommendations
1. Use strong, unique API keys
2. Monitor API usage and costs
3. Set up alerts for unusual activity
4. Regularly update dependencies

## 💰 Cost Optimization

### Free Tier Limits
- **750 hours/month** runtime
- **100GB bandwidth** monthly
- **Shared CPU** resources

### Optimization Tips
1. Implement API rate limiting
2. Cache responses when possible
3. Monitor API usage
4. Use efficient prompts

## 🚀 Post-Deployment

1. **Test all features** on the live URL
2. **Monitor logs** for any errors
3. **Set up alerts** in Render dashboard
4. **Configure custom domain** (optional)
5. **Set up analytics** (optional)

## 📞 Support

- **Render Documentation**: [https://render.com/docs](https://render.com/docs)
- **Groq Documentation**: [https://groq.com/docs](https://groq.com/docs)
- **Tavily Documentation**: [https://tavily.com/docs](https://tavily.com/docs)

---

**Your Legal Assistant is now ready for production deployment on Render.com! 🎉**