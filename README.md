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

The application will:
1. Connect to the Groq API
2. Create an MCP agent
3. Prompt you for your question or request
4. Process your input and display the AI's response

You can ask anything you'd like, for example:
- "Tell me some jokes"
- "What's the weather like?"
- "Give me some recipe ideas"
- "Help me with my homework"

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