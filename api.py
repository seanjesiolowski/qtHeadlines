import requests
import pprint as p


def get_headlines():
    #  This app requires your own api key.  Visit NewsAPI.org.
    api_key = ''

    url = ('https://newsapi.org/v2/top-headlines?'
           'sources=bbc-news&'
           f'apiKey={api_key}')

    r = requests.get(url)

    d = r.json()

    if (r.status_code == 200):
        print("The request was a success!")

        p.pprint(d)

        headlines = []

        for article in d['articles']:
            headline = article['title']
            headlines.append(headline)

    elif (r.status_code == 404):
        print("Result not found!")
        print('Might need to debug something.')

    return headlines
