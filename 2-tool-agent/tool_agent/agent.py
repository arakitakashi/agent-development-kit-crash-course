from datetime import datetime
from google.adk.agents import Agent
from google.adk.tools import google_search

def get_current_time() -> dict:
    # doc string はツールの説明として使用されます。これを元にエージェントがツールを選択します。
    """
    Get the current time in the format YYYY-MM-DD HH:MM:SS
    """
    return {
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

root_agent = Agent(
    name="tool_agent",
    model="gemini-2.0-flash",
    description="Tool agent",
    instruction="""
    You are a helpful assistant that can use the following tools:
    - google_search
    """,
    tools=[google_search], # 使用できるのは１度に１つのツールだけ
    # tools=[get_current_time],
    # tools=[google_search, get_current_time], # <--- Doesn't work
)
