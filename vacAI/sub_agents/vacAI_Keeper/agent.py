from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from google.genai.types import GenerateContentConfig

from vacAI.sub_agents.vacAI_Keeper import prompt


create_reservation = Agent(
    model="gemini-2.5-flash",
    name="create_reservation",
    description="""Create a reservation for the selected item.""",
    instruction=prompt.CONFIRM_RESERVATION_INSTR,
)


payment_choice = Agent(
    model="gemini-2.5-flash",
    name="payment_choice",
    description="""Show the users available payment choices.""",
    instruction=prompt.PAYMENT_CHOICE_INSTR,
)

process_payment = Agent(
    model="gemini-2.5-flash",
    name="process_payment",
    description="""Given a selected payment choice, processes the payment, completing the transaction.""",
    instruction=prompt.PROCESS_PAYMENT_INSTR,
)


vacAI_Keeper = Agent(
    model="gemini-2.5-flash",
    name="vacAI_Keeper",
    description="Given an itinerary, complete the bookings of items by handling payment choices and processing.",
    instruction=prompt.BOOKING_AGENT_INSTR,
    tools=[
        AgentTool(agent=create_reservation),
        AgentTool(agent=payment_choice),
        AgentTool(agent=process_payment),
    ],
    generate_content_config=GenerateContentConfig(
        temperature=0.0, top_p=0.5
    )
)
