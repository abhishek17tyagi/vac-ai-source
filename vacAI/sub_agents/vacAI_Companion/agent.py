from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from google.genai.types import GenerateContentConfig

from vacAI.sub_agents.vacAI_Companion import prompt
from vacAI.tools.memory import memorize
from vacAI.shared_libraries import types

user_special_consideration_agent = Agent(
    model="gemini-2.5-flash",
    name="user_special_consideration_agent",
    description="Establish user special considerations.",
    instruction=prompt.USER_SPECIAL_CONSIDERATION_INSTR,
    generate_content_config=types.json_response_config,
)

user_budget_agent = Agent(
    model="gemini-2.5-flash",
    name="user_budget_agent",
    description="Establish user budget and tracking.",
    instruction=prompt.USER_BUDGET_INSTR,
    tools=[
        AgentTool(agent=user_special_consideration_agent),
    ],
    generate_content_config=types.json_response_config,
)

user_experience_agent = Agent(
    model="gemini-2.5-flash",
    name="user_experience_agent",
    description="Establish user experience and special considerations.",
    instruction=prompt.USER_EXPERIENCE_INSTR,
    tools=[
        AgentTool(agent=user_budget_agent),
    ],
    generate_content_config=types.json_response_config,
)

user_preference_agent = Agent(
    model="gemini-2.5-flash",
    name="user_preference_agent",
    description="Establish user profile and preferences.",
    instruction=prompt.USER_PREFERENCE_INSTR,
    tools=[
        AgentTool(agent=user_experience_agent),
    ],
    generate_content_config=types.json_response_config,
)

user_profile_agent = Agent(
    model="gemini-2.5-flash",
    name="user_profile_agent",
    description="Generate a user profile for the user.",
    instruction=prompt.USER_PROFILE_INSTR,
    tools=[
        AgentTool(agent=user_preference_agent),
    ],
    generate_content_config=types.json_response_config,
)

vacAI_Companion = Agent(
    model="gemini-2.5-flash",
    name="vacAI_Companion",
    description="Coordinate all subagents to build a comprehensive user profile.",
    instruction=prompt.USER_AGENT_INSTR,
    tools=[
        AgentTool(agent=user_profile_agent),
        AgentTool(agent=user_preference_agent),
        AgentTool(agent=user_experience_agent),
        AgentTool(agent=user_special_consideration_agent),
        AgentTool(agent=user_budget_agent),
        memorize
    ],
    generate_content_config=GenerateContentConfig(
        temperature=0.0, top_p=0.5
    )
)
