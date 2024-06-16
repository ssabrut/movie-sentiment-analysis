from dotenv import load_dotenv
from upsert_agent.crew import UpsertAgent
load_dotenv()

# Initialize the tool with a specific CSV file. This setup allows the agent to only search the given CSV file.

def run():
    inputs = {
        'dataset_path': 'data/IMDB Dataset.csv'
    }

    UpsertAgent().crew().kickoff(inputs=inputs)
    # loader = FileReadTool(file_path='data/IMDB Dataset.csv')
    # print(loader.run())

if __name__ == '__main__':
    run()