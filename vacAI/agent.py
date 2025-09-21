from google.adk.agents import Agent

from vacAI import prompt

from vacAI.sub_agents.vacAI_Keeper.agent import vacAI_Keeper
from vacAI.sub_agents.vacAI_Voyager.agent import vacAI_Voyager
from vacAI.sub_agents.vacAI_Spark.agent import vacAI_Spark
from vacAI.sub_agents.vacAI_Weaver.agent import vacAI_Weaver
from vacAI.sub_agents.vacAI_Echo.agent import vacAI_Echo
from vacAI.sub_agents.vacAI_Herald.agent import vacAI_Herald
from vacAI.sub_agents.vacAI_Companion.agent import vacAI_Companion

from vacAI.tools.memory import _load_precreated_itinerary


root_agent = Agent(
    model="gemini-2.5-flash",
    name="vacAI",
    description="A smart travel companion using the services of multiple sub-agents",
    instruction=prompt.ROOT_AGENT_INSTR,
    sub_agents=[
        vacAI_Spark,
        vacAI_Weaver,
        vacAI_Keeper,
        vacAI_Herald,
        vacAI_Voyager,
        vacAI_Echo,
        vacAI_Companion
    ],
    before_agent_callback=_load_precreated_itinerary,
)
