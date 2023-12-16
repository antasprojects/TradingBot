from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from textblob import TextBlob

tickers = [
    "BA",    # Boeing Co.
    "CAT",   # Caterpillar Inc.
    "GS",    # Goldman Sachs Group Inc.
    "HD",    # Home Depot Inc.
    "JPM",   # JPMorgan Chase & Co.
    "KO",    # The Coca-Cola Co.
    "MSFT",  # Microsoft Corp.
    "NKE",   # Nike Inc.
    "V",     # Visa Inc.
    "WMT",   # Walmart Inc.
]

# values used to calculate share of porfolio can be modified to increase or decreaase impact of the sentiment
limit = 0.5
multiplier = 3

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

def get_sentiment_title(title):
    """
    Returns the sentiment polarity for the given title.

    Args:
        title (str): Title of an article.

    Returns:
        float: Sentiment polarity.
    """
    blob = TextBlob(title)
    sentiment = blob.sentiment.polarity
    return(sentiment)

def get_sentiment_ticker(ticker):
    """
    Calculate the average sentiment for a given stock ticker based on scraped article titles.

    Args:
        ticker (str): Ticker symbol of the stock.

    Returns:
        float: Average sentiment value for the given stock ticker, calculated from the sentiment
               of individual article titles related to the stock.
    """

    titles = scraper(ticker)
    sentiments = []

    for title in titles:
        sentiments.append(get_sentiment_title(title))

    average = sum(sentiments) / len(sentiments)

    return average

