from crewai import Agent

data_loading_agent = Agent(
    role='Data Loading Agent',
    goal='Load data from a CSV file',
    backstory='The agent is tasked with loading data from a CSV file. The dataset is located at {dataset_path}',
    allow_delegation=False,
    verbose=True
)