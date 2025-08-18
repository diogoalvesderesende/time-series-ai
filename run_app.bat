@echo off
echo 🚀 Launching Time Series Course Assistant...
echo.

REM Check if virtual environment exists
if not exist "venv" (
    echo ❌ Virtual environment not found!
    echo Please run install.bat first
    pause
    exit /b 1
)

REM Activate virtual environment
echo 📦 Activating virtual environment...
call venv\Scripts\activate.bat

REM Install/upgrade requirements
echo 📚 Installing/upgrading requirements...
pip install -r requirements.txt

REM Launch Streamlit app
echo 🌐 Launching Streamlit app...
echo.
echo 💡 The app will open in your browser at: http://localhost:8501
echo 🛑 Press Ctrl+C to stop the app
echo.
streamlit run streamlit_app.py

pause
