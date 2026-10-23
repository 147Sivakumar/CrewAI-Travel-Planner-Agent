
import os
from crewai import Agent, Task, Crew

# Read the API key and model from environment variables
api_key = os.getenv("OPENAI_API_KEY")
model = os.getenv("MODEL", "openai/gpt-4o-mini")

if not api_key:
    raise EnvironmentError(
        "OPENAI_API_KEY is not set. Please configure your API key."
    )

# Ask the user for a city
city = input("Which city would you like to explore? ").strip()

if not city:
    raise ValueError("Please enter a city name.")

# Create the Travel Planner agent
planner = Agent(
    role="Travel Planner",
    goal="Recommend exactly three interesting places to visit in the city provided by the user.",
    backstory=(
        "You are an experienced travel planner who helps visitors "
        "discover notable attractions. You write for curious travelers "
        "and provide concise descriptions and practical visiting tips."
    ),
    llm=model,
    verbose=True,
)

# Create one task
travel_task = Task(
    description=(
        "Recommend exactly 3 distinct places to visit in {city}. "
        "For each place, provide its name, why it is worth visiting, "
        "and one practical visiting tip. Use a numbered list from 1 to 3."
    ),
    expected_output=(
        "Exactly 3 numbered recommendations. Each must include the "
        "place name, a brief reason to visit, and one practical tip. "
        "Do not include additional attractions or a lengthy introduction."
    ),
    agent=planner,
)

# Create the crew and run the task
crew = Crew(
    agents=[planner],
    tasks=[travel_task],
    verbose=True,
)

result = crew.kickoff(inputs={"city": city})

print("\n=== Your Travel Plan ===\n")
print(result)

