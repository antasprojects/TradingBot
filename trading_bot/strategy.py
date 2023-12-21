from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from textblob import TextBlob
from inputs import limit, multiplier, tickers

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


def get_sentiment_dict(tickers):
    """
    Calculate and return a dictionary of stock tickers mapped to their average sentiment values.

    Args:
        tickers (list): List of stock ticker symbols.

    Returns:
        dict: A dictionary where keys are stock ticker symbols, and values are the corresponding
              average sentiment values, rounded to three decimal places.
    """
    sentiment_dict = {}
    for ticker in tickers:
        sentiment_dict[ticker] = round(get_sentiment_ticker(ticker), 3)
    return sentiment_dict


def get_true_sentiment_dict(sentiment_dict):
    """
    Normalize sentiment values for each stock ticker by subtracting the average sentiment across all tickers.

    Args:
        sentiment_dict (dict): A dictionary where keys are stock ticker symbols, and values are the
                               corresponding average sentiment values.

    Returns:
        dict: A dictionary where keys are stock ticker symbols, and values are the normalized sentiment
              values, rounded to three decimal places.
    """

    true_sentiment_dict = {}
    total = sum(sentiment_dict.values())
    average_sentiment = round(total / len(sentiment_dict), 3)

    for ticker in sentiment_dict:
        true_sentiment_dict[ticker] = round(sentiment_dict[ticker] - average_sentiment, 3)

    return true_sentiment_dict


def portfolio_allocation(true_sentiment_dict):


    """
    Adjust the portfolio allocation based on normalized sentiment values for each stock ticker.

    Args:
        sentiment_dict (dict): A dictionary where keys are stock ticker symbols, and values are the
                               normalized sentiment values.

    Returns:
        dict: A dictionary where keys are stock ticker symbols, and values represent the adjusted
              portfolio allocation percentages for each stock.
    """
    portfolio_allocation = {}

    for ticker, normalized_sentiment in true_sentiment_dict.items():
        stock_share = limit - multiplier * normalized_sentiment
        stock_share = max(0, stock_share)  # Ensure share is not negative.
        portfolio_allocation[ticker] = stock_share

    # Calculate the total adjusted share across all tickers.
    total_share = sum(portfolio_allocation.values())

    # Calculate the percentage allocation for each ticker based on the total adjusted share.
    for ticker in portfolio_allocation:
        percentage_allocation = round(100 * portfolio_allocation[ticker] / total_share, 2)
        portfolio_allocation[ticker] = percentage_allocation

    return portfolio_allocation


def calculate_strategy(tickers):
    """
    Perform sentiment analysis on financial articles and adjust portfolio allocation accordingly.

    Returns:
        dict: A dictionary where keys are stock ticker symbols, and values represent the adjusted
    """ 
    # Step 1: Calculate sentiment values for each stock ticker based on scraped article titles.
    sentiment_dict = get_sentiment_dict(tickers)

    # Step 2: Normalize sentiment values for each stock ticker.
    true_sentiment_dict = get_true_sentiment_dict(sentiment_dict)

    # Step 3: Adjust portfolio allocation based on normalized sentiment values.
    portfolio = portfolio_allocation(true_sentiment_dict)
    return portfolio


if __name__ == "__main__":
    calculate_strategy(tickers)
