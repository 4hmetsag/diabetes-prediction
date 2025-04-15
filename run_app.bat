@echo off
echo Python and required libraries are being checked...
timeout /t 3 > nul

:: Check if python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python.
    pause
    exit /b
) else (
    echo Python is ready.
)

timeout /t 1 > nul

:: Check if numpy is installed
pip show numpy >nul 2>&1
if %errorlevel% neq 0 (
    echo Numpy is not installed, installing...
    pip install numpy==2.2.4
    echo Numpy is installed successfully
) else (
    echo Numpy  is ready.
)

:: Check if pandas is installed
pip show pandas >nul 2>&1
if %errorlevel% neq 0 (
    echo Pandas is not installed, installing...
    pip install pandas==2.2.3
    echo Pandas is installed successfully
) else (
    echo Pandas is ready.
)

:: Check if scikit-learn is installed
pip show scikit-learn >nul 2>&1
if %errorlevel% neq 0 (
    echo scikit-learn is not installed, installing...
    pip install scikit-learn==1.6.1
    echo Scikit-learn is installed successfully
) else (
    echo Scikit-learn is ready.
)

:: Check if streamlit is installed
pip show streamlit >nul 2>&1
if %errorlevel% neq 0 (
    echo Streamlit is not installed, installing...
    pip install streamlit==1.44.1
    echo Streamlit is installed successfully
) else (
    echo Streamlit is ready.
)

:: Check if joblib is installed
pip show joblib >nul 2>&1
if %errorlevel% neq 0 (
    echo joblib is not installed, installing...
    pip install joblib==1.4.2
    echo Joblib is installed successfully
) else (
    echo Joblib is ready.
)

timeout /t 1 > nul

:: Run streamlit app
echo The diabetes prediction app is running...
timeout /t 1 > nul
streamlit run app.py

pause