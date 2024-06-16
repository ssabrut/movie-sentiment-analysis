from crewai import Task
from crewai_tools import FileReadTool

data_loading_task = Task(
    description='Load data from a CSV file. The dataset is located at {dataset_path}',
    expected_output='A JSON object representing the data from the CSV file',
    tools=[FileReadTool()]
)