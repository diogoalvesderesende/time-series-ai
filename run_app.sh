#!/bin/bash

echo "🚀 Launching Time Series Course Assistant..."
echo

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found!"
    echo "Please run install.sh first"
    exit 1
fi

# Activate virtual environment
echo "📦 Activating virtual environment..."
source venv/bin/activate

# Install/upgrade requirements
echo "📚 Installing/upgrading requirements..."
pip install -r requirements.txt

# Launch Streamlit app
echo "🌐 Launching Streamlit app..."
echo
echo "💡 The app will open in your browser at: http://localhost:8501"
echo "🛑 Press Ctrl+C to stop the app"
echo
streamlit run streamlit_app.py
