# AI Assistant

This is an interactive AI-powered application that uses the Groq LLM and MCP agent to respond to your prompts.

## Setup Instructions

1. First, make sure you have Python 3.8+ installed on your system.

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory and add your Groq API key:


## Running the Application

To run the application, simply execute:
```bash
python app.py
```
To exit the application, press Ctrl+C at any time.

## Error Handling

The application includes error handling for:
- Missing API keys
- Configuration issues
- Runtime errors
- Empty or invalid inputs

If you encounter any issues, check:
- Your API key is correctly set in the .env file
- All dependencies are properly installed
- You have an active internet connection 
