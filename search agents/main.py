from dotenv import load_dotenv

load_dotenv()
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage, SystemMessage
from langchain.tools import tool

@tool
def search(query: str) -> str:
    """
    Search the web for the information you need.
    Args:
        query: The query to search for.
    Returns:
        The information found.
    """
    print(f"Searching for {query}")
    return "I found this information for you: Kolkata is old capital of India"
llm = ChatOpenAI(model="gpt-4o-mini")
tools = [search]
agent = create_agent(model=llm, tools=tools)


def main():
    print("Hello from search-agents!")
    result = agent.invoke({"messages": [HumanMessage(content="What is the capital of India?")]})
    print(result)

if __name__ == "__main__":
    main()
