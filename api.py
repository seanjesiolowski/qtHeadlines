import requests
import pprint as p


class APIRequest():
    def __init__(self):
        #  This app requires your own api key.  Visit NewsAPI.org.
        api_key = ''
        url = ('https://newsapi.org/v2/top-headlines?'
               'sources=bbc-news&'
               f'apiKey={api_key}')
        r = requests.get(url)
        self.json_data = r.json()
        if (r.status_code == 200):
            print("The request was a success!")
        elif (r.status_code == 404):
            #  consider a message box here - so user know why headlines aren't showing...
            print("Result not found!")
            print('Might need to debug something.')

    def get_headlines(self):
        headlines = []
        for article in self.json_data['articles']:
            headline = article['title']
            headlines.append(headline)
        return headlines

    def get_description(self, index):
        return self.json_data['articles'][index]['description']


get = APIRequest()
p.pprint(get.json_data)
