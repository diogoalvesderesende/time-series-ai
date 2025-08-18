# 🚀 Time Series Course Assistant - Cyber Diogo

Your AI-powered companion for the best Time Series Course in the world! This chatbot assistant helps you understand time series concepts, find code examples, and get practical guidance on forecasting models.

## ✨ Features

- **🤖 AI-Powered**: Built with state-of-the-art AI models for intelligent responses
- **📚 Course-Aware**: Understands your specific time series curriculum
- **🔍 Smart Search**: Uses vector store to find relevant course content
- **💬 Multi-turn**: Maintains conversation context for better assistance
- **🎯 Practical Focus**: Provides actionable code snippets and explanations
- **🌐 Web Interface**: Beautiful Streamlit app for easy interaction

## 🚀 Quick Start

### Option 1: Automatic Installation (Recommended)

**Windows:**
```bash
install.bat
```

**Linux/Mac:**
```bash
chmod +x install.sh
./install.sh
```

### Option 2: Manual Installation

1. **Create virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# OR
venv\Scripts\activate.bat  # Windows
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Set up your API key:**
   - Create a `.env` file in the project root
   - Add: `OPENAI_API_KEY=your-api-key-here`

## 🌐 Running the Streamlit App

### Option 1: Automatic Launch

**Windows:**
```bash
run_app.bat
```

**Linux/Mac:**
```bash
chmod +x run_app.sh
./run_app.sh
```

### Option 2: Manual Launch

1. **Activate your virtual environment:**
```bash
# Linux/Mac
source venv/bin/activate

# Windows
venv\Scripts\activate.bat
```

2. **Run the Streamlit app:**
```bash
streamlit run streamlit_app.py
```

3. **Open your browser** and go to: `http://localhost:8501`

## 🔑 Setup Requirements

- **Python 3.8+**
- **API Key** - Add to `.env` file
- **Vector Store** - Your course content should be indexed (you already have this!)

## 📚 What You Can Ask

The assistant covers the entire time series curriculum:

- **📊 Time Series Analysis**: EDA, decomposition, ACF/PACF
- **📈 Exponential Smoothing**: SES, DES, TES, Holt-Winters
- **🔄 ARIMA Models**: ARIMA, SARIMA, SARIMAX
- **🔮 Modern Forecasting**: Prophet, Silverkite
- **🧠 Deep Learning**: LSTM, TFT, N-BEATS
- **🤖 GenAI**: Amazon Chronos, Google TSMixer
- **💻 Code Examples**: Python implementations, parameter tuning

### Example Questions:
- "ARIMA vs SARIMA—when to use each?"
- "Show the LSTM code we used"
- "When to use NBEATS vs TFT?"
- "How do we implement cross-validation for time series?"
- "What are the pros/cons of Prophet vs Silverkite?"

## 🛠️ Development

### Project Structure
```
time-series-course-assistant/
├── streamlit_app.py         # Main Streamlit app
├── config.py                # Configuration settings
├── requirements.txt         # Dependencies
├── .env                     # API keys (create this)
├── install.bat              # Windows installer
├── install.sh               # Unix installer
├── run_app.bat              # Windows launcher
├── run_app.sh               # Unix launcher
├── _vector_store.json       # Your course content index
└── README.md                # This file
```

### Adding New Features
1. **Extend the system instructions** in `SYSTEM_INSTRUCTIONS`
2. **Add new tools** to the `tools` list in `ask_bot()`
3. **Customize the assistant personality** in `INITIAL_ASSISTANT_MESSAGE`
4. **Modify UI elements** in the Streamlit app

## 🔧 Troubleshooting

### Common Issues

**"Vector store not available"**
- Ensure `_vector_store.json` exists and contains valid JSON
- Check file permissions

**"API key not found in .env file"**
- Create a `.env` file with `OPENAI_API_KEY=your-key-here`
- Make sure the file is in the project root directory

**"Error communicating with the bot"**
- Check internet connection
- Ensure you have API credits

**Import errors**
- Activate your virtual environment
- Install missing packages: `pip install -r requirements.txt`

**Streamlit not working**
- Make sure you're in the virtual environment
- Check if port 8501 is available
- Try: `streamlit run streamlit_app.py --server.port 8502`

### Getting Help
- Check the console output for specific error messages
- Ensure all dependencies are installed

## 🎯 Next Steps

1. **Test the basic functionality** with simple questions
2. **Explore course content** by asking about specific topics
3. **Customize the assistant** for your specific needs
4. **Add your own course materials** to the vector store
5. **Deploy the Streamlit app** to share with students

## 📝 License

MIT License - Feel free to modify and distribute!

## 🤝 Contributing

Found a bug? Want to add features? Open an issue or submit a pull request!

---

**Happy Time Series Learning! 🎉**

*Powered by AI and your course content*
