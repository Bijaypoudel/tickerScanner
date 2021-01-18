import requests
import json

API_KEY = "tV25M8iOnKJT"
PROJECT_TOKEN = "t0urMZJUevDh"
RUN_TOKEN = "tdqTab7r0T5e"



class Data:
    def __init__(self, api_key, project_token):
        self.api_key = api_key
        self.project_token = project_token
        self.params = {
            "api_key": self.api_key
        }
        self.get_data()

    def get_data(self):
        response = requests.get(f'https://www.parsehub.com/api/v2/projects/{PROJECT_TOKEN}/last_ready_run/data', params = {"api_key": API_KEY})
        self.data = json.loads(response.text)

    def total_tickers(self):
        return len(self.data['Ticker'])


data = Data(API_KEY, PROJECT_TOKEN)

print('Total Stocks per page: ', data.total_tickers())