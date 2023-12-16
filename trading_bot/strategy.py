from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from textblob import TextBlob

def scraper(ticker):
    """
    Scrapes article titles from finviz for the given ticker.

    Args:
        ticker (str): Ticker symbol of the stock.

    Returns:
        list: List of article titles.
    """

    url = "https://finviz.com/quote.ashx?t=" + ticker
    titles = []
    request = Request(url=url, headers={"user-agent": "app"})
    response = urlopen(request)

    soup = BeautifulSoup(response, 'html.parser')

    for link in soup.find_all('a', class_='tab-link-news'):
        titles.append(link.text.strip())


    return titles