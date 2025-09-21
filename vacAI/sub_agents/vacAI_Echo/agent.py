from google.adk.agents import Agent

from vacAI.sub_agents.vacAI_Echo import prompt
from vacAI.tools.memory import memorize

vacAI_Echo = Agent(
    model="gemini-2.5-flash",
    name="vacAI_Echo",
    description="A follow up agent to learn from user's experience; In turn improves the user's future trips planning and in-trip experience.",
    instruction=prompt.POSTTRIP_INSTR,
    tools=[memorize],
)
