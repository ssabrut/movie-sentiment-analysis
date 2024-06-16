from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_groq import ChatGroq

@CrewBase
class UpsertAgent:
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self) -> None:
        self.llm = ChatGroq(temperature=0, model="mixtral-8x7b-32768")

    @agent
    def data_loading_agent(self) -> Agent:
        return Agent(config=self.agents_config['data_loading_agent'], llm=self.llm)

    @task
    def data_loading_task(self) -> Task:
        return Task(config=self.tasks_config['data_loading_task'], agent=self.data_loading_agent())

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=2
        )