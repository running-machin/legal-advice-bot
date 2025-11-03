import os
import re
from flask import Flask, render_template, request, jsonify, session
from flask_session import Session
import requests
import json
from dotenv import load_dotenv
from datetime import timedelta

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Configure session
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = False  # Session expires when browser closes
app.config['SESSION_USE_SIGNER'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=1)  # Backup timeout
Session(app)

def is_legal_related(query):
    """Check if the query is related to legal topics using Groq API"""
    try:
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {os.getenv('GROQ_API_KEY')}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "llama-3.1-8b-instant",
            "messages": [
                {
                    "role": "system",
                    "content": "You are a legal topic classifier. Respond with ONLY 'YES' if the question is about legal topics (laws, rights, contracts, court procedures, legal advice, regulations, etc.) or 'NO' if it's about non-legal topics (weather, jokes, coding, sports, entertainment, etc.). Be strict but fair - borderline legal topics should get 'YES'."
                },
                {
                    "role": "user",
                    "content": f"Is this a legal question: {query}"
                }
            ],
            "max_tokens": 10,
            "temperature": 0.1
        }
        
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        
        data = response.json()
        result = data['choices'][0]['message']['content'].strip().upper()
        
        return result == 'YES'
        
    except Exception as e:
        print(f"Legal detection API error: {e}")
        # Fallback to keyword detection if API fails
        query_lower = query.lower()
        legal_keywords = [
            'law', 'legal', 'lawyer', 'attorney', 'court', 'judge', 'contract', 'agreement',
            'lawsuit', 'litigation', 'statute', 'regulation', 'rights', 'liability', 'damages',
            'plaintiff', 'defendant', 'jurisdiction', 'precedent', 'case law', 'constitutional',
            'criminal', 'civil', 'family law', 'corporate law', 'intellectual property',
            'patent', 'trademark', 'copyright', 'employment law', 'tax law', 'immigration',
            'real estate', 'property law', 'tort', 'negligence', 'breach', 'warranty',
            'lease', 'deed', 'will', 'trust', 'estate', 'bankruptcy', 'divorce', 'custody',
            'adoption', 'marriage', 'domestic', 'harassment', 'discrimination', 'federal',
            'state', 'municipal', 'ordinance', 'code', 'act', 'bill', 'legislation',
            'regulatory', 'compliance', 'violation', 'penalty', 'fine', 'imprisonment',
            'probation', 'parole', 'arrest', 'warrant', 'subpoena', 'evidence', 'testimony',
            'witness', 'jury', 'verdict', 'appeal', 'sentence', 'prosecution', 'defense',
            'legal advice', 'counsel', 'representation', 'retainer', 'bar exam', 'esquire'
        ]
        return any(keyword in query_lower for keyword in legal_keywords)

def call_tavily_search(query):
    """Call Tavily Search API to get relevant context"""
    try:
        url = "https://api.tavily.com/search"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {os.getenv('TAVILY_API_KEY')}"
        }
        
        payload = {
            "query": query,
            "search_depth": "basic",
            "include_answer": True,
            "include_raw_content": False,
            "max_results": 5,
            "include_domains": [],
            "exclude_domains": []
        }
        
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        
        data = response.json()
        
        # Extract relevant context from search results
        context_parts = []
        if 'results' in data:
            for result in data['results'][:3]:  # Use top 3 results
                context_parts.append(f"Source: {result.get('title', 'Unknown')}\n{result.get('content', '')}")
        
        return "\n\n".join(context_parts) if context_parts else "No specific legal context found."
        
    except Exception as e:
        print(f"Tavily API error: {e}")
        return "Unable to retrieve additional legal context at this time."

def call_groq_api(prompt):
    """Call Groq API for LLM inference"""
    try:
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {os.getenv('GROQ_API_KEY')}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "llama-3.1-8b-instant",
            "messages": [
                {
                    "role": "system",
                    "content": "You are a helpful legal assistant. Provide accurate legal information based on the context provided. Always include a disclaimer that this is not legal advice and users should consult with a qualified attorney for specific legal matters. Be clear, concise, and helpful."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "max_tokens": 1000,
            "temperature": 0.3
        }
        
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        
        data = response.json()
        return data['choices'][0]['message']['content']
        
    except Exception as e:
        print(f"Groq API error: {e}")
        return "I apologize, but I'm experiencing technical difficulties. Please try again later."

def build_conversation_context():
    """Build conversation context from session history"""
    if 'history' not in session:
        session['history'] = []
    
    history = session['history']
    if not history:
        return ""
    
    context_lines = ["Previous conversation:"]
    for i, (user_msg, ai_msg) in enumerate(history[-5:]):  # Last 5 exchanges
        context_lines.append(f"User: {user_msg}")
        context_lines.append(f"Assistant: {ai_msg}")
    
    return "\n".join(context_lines)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({'error': 'Message cannot be empty'}), 400
        
        # Check if the query is legal-related
        if not is_legal_related(user_message):
            return jsonify({
                'response': "I can only assist with legal-related questions. Please ask about laws, rights, contracts, court procedures, or similar legal matters.",
                'status': 'restricted'
            })
        
        # Get conversation context
        conversation_context = build_conversation_context()
        
        # Get relevant legal context from Tavily
        legal_context = call_tavily_search(user_message)
        
        # Build the complete prompt
        prompt = f"""Please provide helpful legal information based on the following context and user question.

Relevant Legal Context:
{legal_context}

{conversation_context}

Current User Question: {user_message}

Please provide a clear, informative response that addresses the user's legal question. Include a disclaimer that this is not legal advice. Use **bold** text for important terms and section headers to improve readability."""
        
        # Get response from Groq
        ai_response = call_groq_api(prompt)
        
        # Store conversation in session
        if 'history' not in session:
            session['history'] = []
        
        session['history'].append((user_message, ai_response))
        
        # Keep only last 10 exchanges to prevent session from getting too large
        if len(session['history']) > 10:
            session['history'] = session['history'][-10:]
        
        session.modified = True
        
        return jsonify({
            'response': ai_response,
            'status': 'success'
        })
        
    except Exception as e:
        print(f"Chat endpoint error: {e}")
        return jsonify({'error': 'An unexpected error occurred. Please try again.'}), 500

@app.route('/chat/stream', methods=['POST'])
def chat_stream():
    """Streaming endpoint for real-time chat experience"""
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        
        def generate():
            try:
                # Step 1: Check if legal-related
                yield f"data: {json.dumps({'type': 'status', 'message': 'Checking if this is a legal question...', 'step': 'checking'})}\n\n"
                
                is_legal = is_legal_related(user_message)
                
                if not is_legal:
                    yield f"data: {json.dumps({'type': 'response', 'message': 'I can only assist with legal-related questions. Please ask about laws, rights, contracts, court procedures, or similar legal matters.', 'done': True})}\n\n"
                    return
                
                # Step 2: Get conversation context
                yield f"data: {json.dumps({'type': 'status', 'message': 'Loading conversation context...', 'step': 'context'})}\n\n"
                
                # Get current history from session before streaming
                current_history = session.get('history', [])
                conversation_context = build_conversation_context_from_data(current_history)
                
                # Step 3: Search for legal information
                yield f"data: {json.dumps({'type': 'status', 'message': 'Searching legal databases...', 'step': 'searching'})}\n\n"
                legal_context = call_tavily_search(user_message)
                
                # Step 4: Generate response
                yield f"data: {json.dumps({'type': 'status', 'message': 'Generating legal response...', 'step': 'generating'})}\n\n"
                
                prompt = f"""Please provide helpful legal information based on the following context and user question.

Relevant Legal Context:
{legal_context}

{conversation_context}

Current User Question: {user_message}

Please provide a clear, informative response that addresses the user's legal question. Include a disclaimer that this is not legal advice. Use **bold** text for important terms and section headers to improve readability."""
                
                ai_response = call_groq_api(prompt)
                
                # Step 5: Stream the response
                yield f"data: {json.dumps({'type': 'response_start', 'message': 'Here is your legal information:'})}\n\n"
                
                # Simulate streaming by sending chunks
                words = ai_response.split()
                current_chunk = ""
                chunk_size = 3  # words per chunk
                
                for i, word in enumerate(words):
                    current_chunk += word + " "
                    
                    if (i + 1) % chunk_size == 0 or i == len(words) - 1:
                        yield f"data: {json.dumps({'type': 'chunk', 'message': current_chunk.strip()})}\n\n"
                        current_chunk = ""
                
                # Step 6: Signal completion and provide data for session saving
                yield f"data: {json.dumps({'type': 'session_data', 'user_message': user_message, 'ai_response': ai_response})}\n\n"
                yield f"data: {json.dumps({'type': 'complete', 'done': True})}\n\n"
                
            except Exception as e:
                yield f"data: {json.dumps({'type': 'error', 'message': f'Error: {str(e)}'})}\n\n"
        
        return app.response_class(generate(), mimetype='text/plain')
        
    except Exception as e:
        return jsonify({'error': 'Stream initialization failed'}), 500

@app.route('/save-session', methods=['POST'])
def save_session():
    """Endpoint to save session data after streaming"""
    try:
        data = request.get_json()
        user_message = data.get('user_message', '')
        ai_response = data.get('ai_response', '')
        
        if user_message and ai_response:
            if 'history' not in session:
                session['history'] = []
            
            session['history'].append((user_message, ai_response))
            
            # Keep only last 10 exchanges
            if len(session['history']) > 10:
                session['history'] = session['history'][-10:]
            
            session.modified = True
        
        return jsonify({'success': True})
        
    except Exception as e:
        print(f"Session save error: {e}")
        return jsonify({'error': 'Failed to save session'}), 500

def build_conversation_context_from_data(history):
    """Build conversation context from history data"""
    if not history:
        return ""
    
    context_lines = ["Previous conversation:"]
    for i, (user_msg, ai_msg) in enumerate(history[-5:]):  # Last 5 exchanges
        context_lines.append(f"User: {user_msg}")
        context_lines.append(f"Assistant: {ai_msg}")
    
    return "\n".join(context_lines)

@app.route('/clear', methods=['POST'])
def clear_history():
    """Clear conversation history"""
    session['history'] = []
    session.modified = True
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)