import asyncio
import os
import sys
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from mcp_use import MCPAgent, MCPClient

def setup_environment():
    load_dotenv()
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        print("Error: GROQ_API_KEY not found in environment variables or .env file")
        sys.exit(1)
    os.environ["GROQ_API_KEY"] = api_key

async def open_youtube():
    try:
        client = MCPClient.from_dict('browser-mcp.json')
        await client.navigate('https://www.youtube.com')
        print("YouTube has been opened in your browser")
    except Exception as e:
        print(f"Error opening YouTube: {str(e)}")
        sys.exit(1)

async def create_agent(config_path: str = 'browser-mcp.json'):
    try:
        client = MCPClient.from_dict(config_path)
        llm = ChatGroq(model="gemma2-9b-it")
        return MCPAgent(llm=llm, client=client, max_steps=30)
    except Exception as e:
        print(f"Error creating agent: {str(e)}")
        sys.exit(1)

def get_user_prompt():
    print("\nWhat would you like to ask the AI? (Press Ctrl+C to exit)")
    print("Example: 'Tell me some jokes' or 'What's the weather like?'")
    try:
        return input("\nYour prompt: ").strip()
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)
    except Exception as e:
        print(f"\nError reading input: {str(e)}")
        sys.exit(1)

async def main():
    setup_environment()
    
    # Open YouTube
    await open_youtube()
    
    # Create the agent
    agent = await create_agent()
    
    try:
        # Get prompt from user
        prompt = get_user_prompt()
        if not prompt:
            print("Error: Empty prompt provided")
            return 1
            
        print("\nProcessing your request...")
        result = await agent.run(prompt)
        print("\nAI Response:")
        print("-" * 40)
        print(result)
        print("-" * 40)
        
    except Exception as e:
        print(f"Error during execution: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(asyncio.run(main()))