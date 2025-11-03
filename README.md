# Legal Assistant - RAG Chat Application

A production-ready **Flask** web application that provides legal assistance using Retrieval-Augmented Generation (RAG) with Groq API and Tavily Search API.

## 🚀 **Ready for Render.com Deployment**

This application is **fully configured and ready for deployment** on Render.com. See [DEPLOY.md](DEPLOY.md) for complete deployment instructions.

## Features

- **🤖 RAG Technology**: Combines web search with LLM for accurate, up-to-date legal information
- **🎯 Smart Legal Detection**: Uses AI to detect legal questions instead of simple keyword matching
- **💬 Chat Memory**: Maintains conversation context within the session (auto-clears on browser close)
- **🎨 Premium UI**: Beautiful, modern interface with dark/light mode toggle and animations
- **📱 Mobile-First**: Fully responsive design optimized for all devices
- **⚡ Real-time Streaming**: Server-sent events for live chat experience
- **🌙 Dark Mode**: Toggle between light and dark themes with smooth transitions
- **✨ Rich Text**: Full markdown support with bold text, lists, and formatting
- **🔄 Background Animations**: See what's happening - searching, processing, generating
- **⌨️ Keyboard Shortcuts**: Ctrl+Shift+T (theme), Ctrl+L (clear), Enter (send)
- **🎬 Streaming Effects**: Typing animations and cursor effects for natural chat feel
- **🏥 Production Ready**: Health checks, error handling, security headers, environment variables

## 🌐 **Live Demo**

Deploy your own instance in minutes on Render.com! See [DEPLOY.md](DEPLOY.md) for step-by-step instructions.

## 📋 **Quick Start**

### Local Development

1. **Clone and install**:
   ```bash
   git clone https://github.com/yourusername/legal-assistant.git
   cd legal-assistant
   pip install -r requirements.txt
   ```

2. **Set up environment**:
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

3. **Run locally**:
   ```bash
   python app.py
   # or use: ./start.sh
   ```

4. **Visit**: `http://localhost:5001`

### 🚀 **Deploy to Render.com**

1. **Push to GitHub**
2. **Connect to Render.com**
3. **Set environment variables**
4. **Deploy automatically**

See [DEPLOY.md](DEPLOY.md) for detailed deployment instructions.

## 🏗️ **Technology Stack**

- **Backend**: Flask 2.3.3 (Python)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **AI/LLM**: Groq API (llama-3.1-8b-instant)
- **Search**: Tavily Search API
- **Session**: Flask native sessions (no database required)
- **Deployment**: Render.com compatible

## 📁 **Project Structure**

```
legal-assistant/
├── app.py                 # Main Flask application
├── templates/
│   └── index.html        # Frontend template
├── requirements.txt      # Python dependencies
├── .env.example          # Environment variables template
├── Procfile              # Render process definition
├── runtime.txt           # Python version
├── render.yaml           # Render configuration
├── DEPLOY.md             # Deployment guide
├── README.md             # This file
└── .gitignore            # Git ignore rules
```

## 🎯 **Key Features**

### **AI-Powered Legal Assistance**
- Smart legal question detection using AI
- Real-time web search for current legal information
- Context-aware conversation memory
- Fallback to keyword detection if API unavailable

### **Premium User Experience**
- Beautiful, responsive design
- Dark/light theme toggle
- Real-time streaming responses
- Typing animations and effects
- Mobile-optimized interface

### **Production Ready**
- Health check endpoint
- Environment variable configuration
- Security headers and HTTPS support
- Error handling and graceful fallbacks
- Auto-deployment ready

## Usage

1. Open your browser and go to `http://localhost:5001`
2. Ask legal questions about laws, rights, contracts, court procedures, etc.
3. The assistant will search for current legal information and provide helpful responses
4. Non-legal questions will be rejected with a restriction message
5. Use the "Clear" button to reset the conversation history

## Example Questions

- "What are the basic elements of a contract?"
- "How does copyright protection work?"
- "What should I do if I'm involved in a car accident?"
- "What is the difference between civil and criminal law?"
- "How do I file for divorce?"

## Important Notes

- **This is not legal advice**: The application provides general legal information and always includes a disclaimer
- **Session-based memory**: Conversation history is only stored for the current browser session
- **Legal topics only**: The chatbot is restricted to legal-related questions only
- **API limits**: Be aware of your API usage limits for both Groq and Tavily

## File Structure

```
.
├── .env.example           # Example environment variables file
├── app.py                 # Flask backend application
├── templates/
│   └── index.html        # Frontend chat interface
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Technical Details

- **Backend**: Flask with simple session management and Server-Sent Events (SSE)
- **LLM**: Groq API using llama-3.1-8b-instant model
- **Smart Detection**: AI-powered legal question classification
- **Search**: Tavily Search API for real-time legal context
- **Frontend**: Modern HTML5/CSS3/JavaScript with streaming support
- **Memory**: Flask session with auto-clear on browser close (no filesystem dependency)
- **UI/UX**: Premium responsive design with animations and micro-interactions
- **Streaming**: Real-time text streaming with typing effects
- **Markdown**: Full markdown rendering for rich text display

## Troubleshooting

1. **API Key Errors**: Make sure your environment variables are set correctly in `.env` file
2. **Groq API 400 Error**: Ensure you're using a valid model name like `llama-3.1-8b-instant`
3. **Import Errors**: Ensure all dependencies are installed with `pip install -r requirements.txt`
4. **Port Issues**: If port 5001 is in use, modify the `port` parameter in `app.py`
5. **Session Issues**: Chat history automatically clears when browser closes (no filesystem needed)
6. **Dark Mode Issues**: Theme preference is stored in localStorage, clear browser data if needed
7. **Streaming Issues**: If streaming doesn't work, app automatically falls back to regular responses
8. **Mobile Issues**: App is fully responsive - refresh page if layout issues occur
9. **Cookie Errors**: Fixed - simplified session management eliminates encoding issues

## License

This project is for educational purposes. Use responsibly and in compliance with the terms of service of the APIs used.