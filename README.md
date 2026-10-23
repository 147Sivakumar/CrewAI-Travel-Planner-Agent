# CrewAI Travel Planner Agent

A simple AI-powered travel planner built using Python and CrewAI. The agent takes a city name from the user and recommends exactly three places to visit, with a short explanation and a practical visiting tip for each place.

## Project Overview

This project demonstrates how to build your first CrewAI agent using an Agent, a Task, and a Crew. It uses an OpenAI language model to generate travel recommendations based on the city entered by the user.

## Features

- Accepts a city name through user input.
- Uses one Travel Planner agent.
- Provides exactly three sightseeing recommendations.
- Includes a reason to visit and a practical tip for each place.
- Displays verbose execution logs.
- Reads the API key from an environment variable.

## Technologies Used

- Python
- CrewAI
- OpenAI API
- `openai/gpt-4o-mini` model by default

## Project Structure

```text
CrewAI Travel Planner Agent/
├── travel_planner.py
├── README.md
├── .gitignore
└── venv/
```

The `venv/` directory contains the local Python virtual environment and should not be uploaded to GitHub.

## Prerequisites

- Python installed on your computer.
- An OpenAI API key with access to the selected model.
- PowerShell on Windows, or a compatible terminal on macOS/Linux.

## Installation and Setup

### 1. Create a virtual environment

```powershell
python -m venv venv
```

### 2. Activate the virtual environment

On Windows PowerShell:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
```

On macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Install CrewAI

```bash
python -m pip install crewai
```

### 4. Configure environment variables

On Windows PowerShell:

```powershell
$env:OPENAI_API_KEY="your-actual-api-key"
$env:MODEL="openai/gpt-4o-mini"
```

On macOS/Linux:

```bash
export OPENAI_API_KEY="your-actual-api-key"
export MODEL="openai/gpt-4o-mini"
```

Replace `your-actual-api-key` with your own API key. Never publish your API key or commit it to GitHub.

## How to Run

Run the following command from the project directory:

```bash
python travel_planner.py
```

Enter a city when prompted:

```text
Which city would you like to explore? Chennai
```

The agent will execute the task and print three travel recommendations.

## Example Output

```text
=== Your Travel Plan ===

1. Marina Beach
   Worth Visiting: Enjoy the beach, local snacks, and the lively atmosphere.
   Practical Tip: Visit early in the morning or late in the evening.

2. Kapaleeshwarar Temple
   Worth Visiting: Explore traditional Dravidian architecture and local culture.
   Practical Tip: Dress modestly when visiting the temple.

3. Government Museum
   Worth Visiting: Discover historical artifacts, art, and natural history exhibits.
   Practical Tip: Allow enough time to explore the museum.
```

*Example output is illustrative. Actual recommendations may vary.*

## How It Works

1. The program asks the user to enter a city.
2. The Travel Planner agent receives a clearly defined role, goal, and backstory.
3. A single task instructs the agent to recommend exactly three places.
4. The Crew combines the agent and task.
5. `crew.kickoff(inputs={"city": city})` executes the task.
6. The program prints the final recommendations.

## Security

The OpenAI API key is read from the `OPENAI_API_KEY` environment variable. It is not stored in the Python source code.

Recommended `.gitignore`:

```gitignore
venv/
.env
__pycache__/
*.pyc
```

## Learning Objectives

- Create a CrewAI agent with a role, goal, and backstory.
- Define a task with a clear description and expected output.
- Assemble an agent and task into a Crew.
- Execute a Crew using `crew.kickoff()`.
- Configure environment variables securely.

## Author

Created as part of a CrewAI learning assignment.

## License

This project is intended for educational and learning purposes.
