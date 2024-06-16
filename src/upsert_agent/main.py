from crewai import Crew, Task
from crewai_tools import FileReadTool
from dotenv import load_dotenv
load_dotenv()

def run():    
    data_loading_task = Task(
        description='Load data from a CSV file. The dataset is located at data/IMDB Dataset.csv',
        expected_output='A JSON object representing the data from the CSV file',
        agent=data_loading_agent,
        tools=[FileReadTool()]
    )
    
    crew = Crew(
        tasks=[data_loading_task],
        agents=[data_loading_agent],
        verbose=2
    )

    result = crew.kickoff()
    print(result)

if __name__ == '__main__':
    run()