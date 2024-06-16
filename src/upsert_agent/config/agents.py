from crewai import Agent
from langchain_groq import ChatGroq

llm = ChatGroq(temperature=0, model="mixtral-8x7b-32768")
data_loading_agent = Agent(
    role='Data Loading Agent',
    goal='Load data from a CSV file',
    backstory="""The agent is tasked with loading data from a CSV file. The dataset is located at data/IMDB Dataset.csv""",
    llm=llm,
    verbose=True
)