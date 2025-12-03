import requests
from bs4 import BeautifulSoup

url = "https://www.indiatoday.in/latest-news"

def get_latest_news(url):

    responce = requests.get(url)
    soup = BeautifulSoup(responce.text, 'html.parser')

    headlines = soup.find_all('h2')

    for idx, headline in enumerate(headlines, start=1):

        print(f"{idx}. {headline.text.strip()}")

get_latest_news(url)