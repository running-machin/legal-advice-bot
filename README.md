# Legal Assistant - RAG Chat Application

A minimal Flask web application that provides legal assistance using Retrieval-Augmented Generation (RAG) with Groq API and Tavily Search API.

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

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Environment Variables

You can set environment variables in two ways:

**Option A: Using .env file (Recommended)**

1. Copy the example file:
```bash
cp .env.example .env
```

2. Edit the `.env` file and add your API keys:
```
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

**Option B: Using environment variables**

**For Linux/macOS:**
```bash
export GROQ_API_KEY="your_groq_api_key_here"
export TAVILY_API_KEY="your_tavily_api_key_here"
```

**For Windows (Command Prompt):**
```cmd
set GROQ_API_KEY=your_groq_api_key_here
set TAVILY_API_KEY=your_tavily_api_key_here
```

**For Windows (PowerShell):**
```powershell
$env:GROQ_API_KEY="your_groq_api_key_here"
$env:TAVILY_API_KEY="your_tavily_api_key_here"
```

### 3. Get API Keys

- **Groq API Key**: Sign up at [https://groq.com/](https://groq.com/) and get your API key from the dashboard
- **Tavily API Key**: Sign up at [https://tavily.com/](https://tavily.com/) and get your API key from the dashboard

### 4. Run the Application

```bash
python app.py
```

The application will start on `http://localhost:5001`

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

- **Backend**: Flask with session management and Server-Sent Events (SSE)
- **LLM**: Groq API using llama-3.1-8b-instant model
- **Smart Detection**: AI-powered legal question classification
- **Search**: Tavily Search API for real-time legal context
- **Frontend**: Modern HTML5/CSS3/JavaScript with streaming support
- **Memory**: Flask session with auto-clear on browser close
- **UI/UX**: Premium responsive design with animations and micro-interactions
- **Streaming**: Real-time text streaming with typing effects
- **Markdown**: Full markdown rendering for rich text display

## Troubleshooting

1. **API Key Errors**: Make sure your environment variables are set correctly in `.env` file
2. **Groq API 400 Error**: Ensure you're using a valid model name like `llama-3.1-8b-instant`
3. **Import Errors**: Ensure all dependencies are installed with `pip install -r requirements.txt`
4. **Port Issues**: If port 5001 is in use, modify the `port` parameter in `app.py`
5. **Session Issues**: Chat history automatically clears when browser closes
6. **Dark Mode Issues**: Theme preference is stored in localStorage, clear browser data if needed
7. **Streaming Issues**: If streaming doesn't work, app automatically falls back to regular responses
8. **Mobile Issues**: App is fully responsive - refresh page if layout issues occur
9. **Flask Context Errors**: Fixed - session management now works properly with streaming

## License

This project is for educational purposes. Use responsibly and in compliance with the terms of service of the APIs used.