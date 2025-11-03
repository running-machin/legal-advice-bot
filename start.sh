#!/bin/bash

echo "🚀 Starting Legal Assistant for Local Testing"
echo "=========================================="

# Check if .env file exists
if [ ! -f .env ]; then
    echo "⚠️  .env file not found. Creating from template..."
    cp .env.example .env
    echo "📝 Please edit .env file with your API keys:"
    echo "   - GROQ_API_KEY=your_groq_api_key_here"
    echo "   - TAVILY_API_KEY=your_tavily_api_key_here"
    echo ""
    echo "Then run this script again."
    exit 1
fi

# Check if API keys are set
source .env
if [ -z "$GROQ_API_KEY" ] || [ "$GROQ_API_KEY" = "your_groq_api_key_here" ]; then
    echo "⚠️  Please set your GROQ_API_KEY in .env file"
    exit 1
fi

if [ -z "$TAVILY_API_KEY" ] || [ "$TAVILY_API_KEY" = "your_tavily_api_key_here" ]; then
    echo "⚠️  Please set your TAVILY_API_KEY in .env file"
    exit 1
fi

echo "✅ Environment variables configured"
echo "🌐 Starting Flask development server..."
echo "📱 App will be available at: http://localhost:5001"
echo "🛑 Press Ctrl+C to stop"
echo ""

# Start the Flask app
python app.py