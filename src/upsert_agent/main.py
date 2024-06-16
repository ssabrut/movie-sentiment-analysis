from dotenv import load_dotenv
from upsert_agent.crew import UpsertAgent
load_dotenv()

def run():
    inputs = {
        'dataset_path': 'data/IMDB Dataset.csv'
    }

    UpsertAgent().crew().kickoff(inputs=inputs)
    # loader = CSVLoader(file_path='data/IMDB Dataset.csv')
    # data = loader.load()
    # print(data[0].page_content)

if __name__ == '__main__':
    run()