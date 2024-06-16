from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_groq import ChatGroq
from upsert_agent.config.agents import data_loading_agent
from upsert_agent.config.tasks import data_loading_task

class UpsertAgent():
    def crew(self) -> Crew:
        return Crew(
            agents=[data_loading_agent],
            tasks=[data_loading_task],
            verbose=2
        )