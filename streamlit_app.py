#!/usr/bin/env python3
"""
Time Series Course Assistant - Streamlit App
Cyber Diogo's AI-powered course helper
"""

import streamlit as st
import json
import os
from pathlib import Path
from typing import Optional
import time
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI
from streamlit_extras.buy_me_a_coffee import button

# Load environment variables from .env file
load_dotenv(override=True)

# Debug: Check what API key is loaded
api_key = os.getenv("OPENAI_API_KEY")

# Configure OpenAI client
client = OpenAI(api_key=api_key)

# Page configuration
st.set_page_config(
    page_title="Time Series Course Assistant",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    /* optional: tighten section gaps */
    section.main > div { padding-top: 0.25rem; }
    .main-header {
        /* Main title - largest and most prominent */
        font-size: clamp(2.5rem, 6vw, 3rem) !important;
        font-weight: 900;
        color: #0074FF;
        text-align: center;
        margin-bottom: 1.5rem;
        word-wrap: break-word;
        overflow-wrap: break-word;
        max-width: 100%;
        line-height: 1.1;
        padding: 0 0.5rem;
        white-space: normal;
        overflow: visible;
        letter-spacing: -0.02em;
    }
    
    /* Tagline styling */
    .tagline {
        font-size: clamp(1.1rem, 2.5vw, 1.3rem) !important;
        font-weight: 400;
        color: #666666;
        text-align: center;
        margin-bottom: 2.5rem;
        line-height: 1.4;
    }
    
    /* Welcome section styling */
    .welcome-section {
        margin-bottom: 2rem;
    }
    
    .welcome-title {
        font-size: clamp(1.6rem, 3.5vw, 2rem) !important;
        font-weight: 700;
        color: #373435;
        margin-bottom: 1rem;
        line-height: 1.3;
    }
    
    .welcome-intro {
        font-size: clamp(1rem, 2vw, 1.1rem) !important;
        font-weight: 400;
        color: #555555;
        margin-bottom: 1.5rem;
        line-height: 1.5;
    }
    
    .capabilities-list {
        font-size: clamp(0.95rem, 1.8vw, 1rem) !important;
        line-height: 1.6;
        margin-bottom: 1.5rem;
        color: #373435;
    }
    
    .capabilities-list strong {
        font-weight: 600;
        color: #373435;
    }
    
    .capabilities-list ul {
        margin: 0;
        padding-left: 1.5rem;
    }
    
    .capabilities-list li {
        margin-bottom: 0.5rem;
        padding-left: 0.5rem;
    }
    
    .call-to-action {
        font-size: clamp(1rem, 2vw, 1.1rem) !important;
        font-weight: 500;
        color: #000000;
        font-style: italic;
        margin-top: 1.5rem;
    }
    
    /* Enhanced message styling */
    .user-message {
        background: linear-gradient(135deg, rgba(255, 255, 51, 0.2), rgba(0, 116, 255, 0.15));
        border-radius: 15px;
        padding: 10px 14px;
        margin: 4px 0;
        border-left: 4px solid #0074FF;
        text-align: right;
        margin-left: 20%;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        color: #373435;
        backdrop-filter: blur(5px);
        border: none;
        outline: none;
    }
    
    .assistant-message {
        background: linear-gradient(135deg, rgba(112, 95, 254, 0.2), rgba(255, 255, 51, 0.15));
        border-radius: 15px;
        padding: 10px 14px;
        margin: 4px 0;
        border-left: 4px solid #705FFE;
        text-align: left;
        margin-right: 20%;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        color: #373435;
        border: 1px solid rgba(112, 95, 254, 0.3);
        backdrop-filter: blur(5px);
    }
    
    /* Code block styling */
    .code-block {
        background-color: #f8f9fa;
        border: 1px solid #e9ecef;
        border-radius: 8px;
        padding: 12px;
        font-family: 'Courier New', monospace;
        margin: 8px 0;
        position: relative;
    }
    
    /* Quick action buttons */
    .quick-action-btn {
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 20px;
        padding: 8px 16px;
        margin: 4px;
        cursor: pointer;
        font-size: 14px;
        transition: all 0.3s ease;
    }
    
    .quick-action-btn:hover {
        background-color: #0056b3;
        transform: translateY(-1px);
    }
    
    /* Better button styling */
    .stButton > button {
        border-radius: 15px;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        background-color: #0074FF !important;
        color: white !important;
        border: none !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        background-color: #0049DC !important;
    }
    
    /* Override Streamlit's primary button colors */
    .stButton > button[data-baseweb="button"],
    .stButton > button[data-testid="stFormSubmitButton"],
    .stButton > button[type="submit"] {
        background-color: #0074FF !important;
        color: white !important;
        background-image: none !important;
    }
    
    /* Electric blue send button - target form submit buttons specifically */
    .stFormSubmitButton > button,
    .stFormSubmitButton button,
    form button[type="submit"],
    .stButton > button[data-testid="stFormSubmitButton"] {
        background-color: #0074FF !important;
        color: white !important;
        border: none !important;
        background-image: none !important;
    }
    
    /* Override any Streamlit default button colors */
    button[data-baseweb="button"] {
        background-color: #0074FF !important;
        color: white !important;
    }
    
    /* Improved text input */
    .stTextArea > div > div > textarea {
        border-radius: 15px;
        border: 3px solid #E0E0E0;
        transition: border-color 0.0s ease;
    }
    
    .stTextArea > div > div > textarea:focus {
        border-color: #0074FF;
        box-shadow: 0 0 0 2px rgba(0, 116, 255, 0.2);
    }
    
    /* Kill ALL borders and shadows around the text area wrapper */
    .stTextArea, 
    .stTextArea > div, 
    .stTextArea > div > div {
        border: none !important;
        outline: none !important;
        box-shadow: none !important;
        background: transparent !important; /* or white if you prefer */
    }
            
    .stTextArea > div > div > textarea {
        font-family: 'Montserrat', sans-serif !important;
        color: #373435 !important;  /* dark gray body text */
        background-color: #FFFFFF !important; /* clean white input */
        border-radius: 15px !important;
        border: 2px solid #E0E0E0 !important; /* soft gray border */
    }
    .stTextArea > div > div > textarea:focus {
        border-color: #0074FF !important;  /* brand blue focus */
        box-shadow: 0 0 0 2px rgba(0, 116, 255, 0.2) !important;
    }

    

</style>
""", unsafe_allow_html=True)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "last_response_id" not in st.session_state:
    st.session_state.last_response_id = None
if "vector_store_id" not in st.session_state:
    st.session_state.vector_store_id = None


# Load vector store metadata
def load_vector_store():
    """Load the vector store ID from the JSON file."""
    try:
        current_dir = Path(__file__).parent
        vector_store_path = current_dir / "_vector_store.json"
        
        if vector_store_path.exists():
            with open(vector_store_path, 'r') as f:
                vs_meta = json.load(f)
            return vs_meta.get("id")
        else:
            st.error("❌ Vector store file not found. Please ensure _vector_store.json exists.")
            return None
    except Exception as e:
        st.error(f"❌ Error loading vector store: {e}")
        return None

# Get API key from .env file
def get_api_key():
    """Get API key from .env file."""
    return os.getenv("OPENAI_API_KEY")

def display_message(role, content, timestamp=None):
    """Display a message with proper styling and metadata"""
    def clean(txt: str) -> str:
        # remove both raw and escaped <br> variants
        replacements = [
            '<br>', '<br/>', '<br />',
            '&lt;br&gt;', '&lt;br/&gt;', '&lt;br /&gt;'
        ]
        for r in replacements:
            txt = txt.replace(r, '')
        return txt.strip()

    safe = clean(content)

    if role == "user":
        st.markdown(f"""
        <div class="user-message">
            <strong>You</strong>{f' <small style="color:#666;">{timestamp}</small>' if timestamp else ''}
            <br>{safe}
        </div>
        """, unsafe_allow_html=True)
    else:
        # Assistant content can include HTML formatting—keep as is
        st.markdown(f"""
        <div class="assistant-message">
            <strong>Assistant</strong>{f' <small style="color:#666;">{timestamp}</small>' if timestamp else ''}
            <br>{content}
        </div>
        """, unsafe_allow_html=True)



def display_code_snippet(code, language="python", filename=None):
    """Display code with syntax highlighting and copy button"""
    st.markdown(f"""
    <div class="code-block">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
            <strong>{filename or 'Code Snippet'}</strong>
            <button onclick="navigator.clipboard.writeText(`{code}`)" class="quick-action-btn">
                📋 Copy
            </button>
        </div>
        <pre><code class="language-{language}">{code}</code></pre>
    </div>
    """, unsafe_allow_html=True)

def process_user_input(user_input):
    """Process user input and generate response"""
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
        
    # Get bot response
    with st.spinner("🤔 Thinking..."):
        response = ask_bot(user_input)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Rerun to show new messages
    st.rerun()

# System instructions
SYSTEM_INSTRUCTIONS = """
You are Cyber Diogo, the assistant for the best "Time Series Course" in the world.
Be concise, direct, and practical. Use active voice. No fluff.

Primary objective
- Answer questions about the course content and code using the attached Vector Store (transcripts and .py files).
- Prefer retrieved facts over memory. If the files don't cover it, say so.

Retrieval & citations
- Always use File Search first.
- Ground every substantive answer in retrieved snippets.
- If nothing relevant is found, say: "I don't see this in the course files." Then propose the most likely Sections.

Answer style
- Keep outputs scannable: short paragraphs, bullets for steps, and minimal runnable code blocks for Python.
- If "how to do X in Python", show a small snippet with imports and comments.
- End by asking a question to the user that could be asked in the future.
- write like talking to a friend. Be approachable, friendly, fun.

Boundaries
- Don't invent references or numbers.
- If the question is off-scope (not time series/Python/this curriculum), ask a brief clarifying question or answer at a high level and flag it as outside the course corpus.

Context: Course map & typical intents
- Part 1: Time Series Analysis (EDA, time index, data manipulation, visualization, decomposition, ACF/PACF, role play, "useful functions" script, section recap, pitfalls case study).
- Exponential Smoothing & Holt-Winters: SES, DES, TES; train/test split; metrics (MAE, RMSE, MAPE); daily data; "predicting the future"; pros/cons; capstone "Air miles".
- ARIMA/SARIMA/SARIMAX: stationarity, AR/MA/ARIMA, AIC/BIC, SARIMA, SARIMAX with exogenous regressors, CV, parameter tuning (setup, results), future prediction setup, Q&A highlight on future data; pros/cons.
- Part 2: Modern Forecasting — Prophet: structural TS, holidays/regressors, CV, metrics, fixing anomalies, feature engineering, tuning, forecasting, visualization; pros/cons; capstone challenges.
- Part 3: Deep Learning — LSTM: RNN/LSTM basics, data prep/time covariates/scaling, model/training, CV, parameter grids/tuning rounds, multi-series (M4), visualization of results, forecasting; pros/cons.
- TFT (Temporal Fusion Transformers): covariates (past/future/static), scaling, model params, training/CV, tuning, forecasting/interpretability, key takeaways; multi-series TFT capstone.
- N-BEATS: architecture, series/covariates/scaling, params, model training, CV, tuning and best params, forecasting; pros/cons and learnings.
- GenAI for Time Series: Amazon Chronos — setup, params, model, CV, tuning, visualization; pros/cons and learnings.
- Google TSMixer: setup, data processing, params, model, CV, tuning, forecasting, key learnings.
- LinkedIn Silverkite: model components (growth, seasonality, changepoints, regressors/lagged), CV, tuning, visualization; Prophet vs Silverkite notes; warnings/changes.
- Capstones: Holt-Winters (Air miles), Prophet, Multiple Series with TFT, Automated TS Forecasting pipeline.
- Appendix: Python & Pandas refreshers (I/O, cleaning, manipulation, analysis, viz) and fundamentals (types, ops, loops, dicts, functions), plus challenges and labs.

What to prioritize per topic
- Definitions & when-to-use: ARIMA vs SARIMA vs SARIMAX; SES/DES/TES selection; Prophet vs Silverkite; LSTM/TFT/N-BEATS differences.
- Practical steps: train/test split for TS, cross-validation methods, parameter grids, evaluation (MAE/RMSE/MAPE), handling seasonality/holidays/regressors, dealing with future covariates.
- Code pointers: "Show the Holt-Winters code", "Where do we compute MAPE?", "How is CV implemented?", "How are exogenous regressors added in SARIMAX?", "How do we scale/features for LSTM/TFT?"

If the user references a lecture/section by name/number, search for files whose names contain that stem and focus your answer there.
NEVER use specific lecture numbers or titles in your answers as they change.
"""

INITIAL_ASSISTANT_MESSAGE = """
I'm Cyber Diogo, your Time Series assistant! 🚀
Ask me anything about the course or code—models, tuning, or "why did we do X here?"
Try: "ARIMA vs SARIMA—when to use each?", "Show the LSTM code we used", or "When to use NBEATS vs TFT?"
"""

# OpenAI client setup
def ask_bot(user_question: str, verbosity: str = "low"):
    common_kwargs = {
        "model": "gpt-5-nano",
        "tools": [{"type": "file_search", "vector_store_ids": [st.session_state.vector_store_id]}],
        "text": {"verbosity": verbosity}
        }

    if st.session_state.last_response_id:
        # Continue the same conversation on the server
        resp = client.responses.create(
            previous_response_id=st.session_state.last_response_id,
            input=[{"role": "user", "content": user_question}],
            **common_kwargs,
        )
    else:
        # First turn: seed with system + initial assistant message
        resp = client.responses.create(
            input=[
                {"role": "system", "content": SYSTEM_INSTRUCTIONS},
                {"role": "assistant", "content": INITIAL_ASSISTANT_MESSAGE},
                {"role": "user", "content": user_question},
            ],
            **common_kwargs,
        )

    st.session_state.last_response_id = resp.id
    print(resp.output_text)
    return resp.output_text

def reset_conversation():
    """Reset the conversation history."""
    st.session_state.last_response_id = None
    st.session_state.messages = []
    st.rerun()

# Main app
def main():
    # Header
    st.markdown('<h1 class="main-header">🚀 Time Series Course Assistant</h1>', unsafe_allow_html=True)
    st.markdown('<p class="tagline">Your AI sidekick Cyber Diogo - because every data scientist needs a trusty companion! 🤖🦸‍♂️</p>', unsafe_allow_html=True)
    
    # Introduction section
    with st.expander("📚 What I Can Help You With", expanded=False):
        st.markdown("""
        **🎯 My Capabilities:**
        - **Code Snippets**: Get ready-to-run Python code for any time series model
        - **Concept Explanations**: Understand ARIMA vs SARIMA, when to use each, etc.
        - **File References**: I'll pull exact content from course files with citations
        - **Multi-turn Conversations**: Ask follow-ups and I'll remember context
        - **Practical Examples**: Real-world applications and best practices
        
        **📖 Course Topics I Cover:**
        - **Part 1**: Introduction to Time Series: EDA, Exponential Smoothing, ARIMA, SARIMA and SARIMAX
        - **Part 2**: Modern Time Series: Prophet and Intermittent Time Series           
        - **Part 3**: Deep Learning (LSTM, TFT, N-BEATS), 
        - **Part 4** Advanced Time Series: GenAI (Chronos, TSMixer), Time Series for Classification
        - **Capstone Projects**: Complete projects and real-world applications
        - **Graveyard**: Models that used to be popular but are now deprecated like Silverkite.
        
        **❌ What I Cannot Do:**
        - Run code or execute scripts (I provide code, you run it)
        - Access external websites or real-time data
        - Remember conversations between sessions
        - Provide financial or medical advice
        - Solve problems outside the course scope
        """)
    

    
    # Load vector store
    if not st.session_state.vector_store_id:
        st.session_state.vector_store_id = load_vector_store()
    
    # Sidebar
    with st.sidebar:
        st.header("⚙️ Settings")
        
        # Reset button
        if st.button("🔄 Reset Conversation", type="secondary"):
            reset_conversation()
        
        st.markdown("---")
        
        # Support section
        st.markdown("### 💝 Support This App")
        st.markdown("Help keep this Time Series Course Assistant free and running!")
        
        # Buy Me a Coffee button
        button(
            username="diogoalvesx",  # Replace with your actual username
            floating=True,
            text="Buy me a coffee",
            emoji="☕",
            bg_color="#0074FF",  # Your brand blue
            font_color="#FFFFFF",  # White text
            coffee_color="#FFFFFF",  # White coffee icon
            width=300
        )
        

    
    # Welcome message and capabilities - always visible
    st.markdown('<div class="welcome-section">', unsafe_allow_html=True)
    st.markdown('<h2 class="welcome-title">🦸‍♂️ Ready to Predict the Future?</h2>', unsafe_allow_html=True)
    st.markdown('<p class="welcome-intro">Your AI sidekick Cyber Diogo is here to assist you with:</p>', unsafe_allow_html=True)
    st.markdown("""
    <div class="capabilities-list">
    <ul>
    <li><strong>⚡ Code Mastery:</strong> Ready-to-deploy examples for Holt-Winters, ARIMA, Prophet, LSTM, TFT, N-BEATS</li>
    <li><strong>🎯 Strategic Insights:</strong> When to use each model and why - no more guesswork</li>
    <li><strong>🚀 Pro Techniques:</strong> Train/test splits, cross-validation, and parameter tuning that actually work</li>
    <li><strong>📚 Deep Knowledge:</strong> Direct access to course materials and real-world applications</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('<p class="call-to-action">How can I help you? 🚀</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Main chat area - show messages when they exist
    if st.session_state.messages:
        # Add some spacing before chat messages
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Display chat messages with enhanced styling
        for i, message in enumerate(st.session_state.messages):
            # Add timestamp for recent messages
            timestamp = None
            if i == len(st.session_state.messages) - 1:
                timestamp = datetime.now().strftime("%H:%M")
            
            display_message(message["role"], message["content"], timestamp)
    
    # Enhanced chat input at the bottom
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        with st.form("chat_form", clear_on_submit=True):
            user_input = st.text_area(
                "Your question:",
                placeholder="Enter your message here....",
                key="user_input",
                height=80,
                label_visibility="collapsed"
            )
            
            submitted = st.form_submit_button("🚀 Send", use_container_width=True, type="primary", help="Send your message")
            if submitted and user_input.strip():
                process_user_input(user_input.strip())

if __name__ == "__main__":
    main()
