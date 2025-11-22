"""
Hugging Face Spaces entry point for Streamlit
This file is used when deploying to Hugging Face Spaces
"""
# For Hugging Face Spaces, we can directly use streamlit_app.py
# But if we need app.py as entry point, we'll import everything

# Read and execute the streamlit_app.py file
import sys
from pathlib import Path

# Add current directory to path
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

# Execute the streamlit app
streamlit_app_path = current_dir / "streamlit_app.py"
if streamlit_app_path.exists():
    with open(streamlit_app_path, 'r', encoding='utf-8') as f:
        code = f.read()
    exec(code)
else:
    # Fallback: try importing
    import streamlit_app

