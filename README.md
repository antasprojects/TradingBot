This Python script is a portfolio management system that uses sentiment analysis to dynamically adjust the portfolio allocation for a list of selected stocks. The system reads configuration details from the provided file, allowing users to customize their investment amount, list of stocks, and parameters influencing sentiment-based portfolio adjustments. To execute the portfolio management system, run the main script (main.py) after configuring the parameters in inputs.py. Then the program analyzes to adjust the account's portfolio, prompting the user for confirmation before executing any trades.

	Configuration File - inputs.py

Serves as the primary input for the portfolio management system. Users can modify the following parameters based on their preferences:
Investment - variable to reflect the desired total capital available for your portfolio in GBP.

tickers - list to include the stock symbols for the companies you want to include in your portfolio.

limit and multiplier - variables to change the impact of sentiment on your portfolio allocation. A higher multiplier will result in more substantial adjustments based on sentiment values.

	Sentiment Analysis - strategy.py
This Python script performs sentiment analysis on financial articles related to a list of selected stocks. It uses web scraping to retrieve article titles, analyzes the sentiment of each title, and then calculates the portfolio with given stocks according to the formula. It contains the following functions:

scraper(ticker)
Scrapes article titles from finviz for the given stock ticker.

get_sentiment_title(title)
Returns the sentiment polarity for the given article title.

get_sentiment_ticker(ticker)
Calculates the average sentiment for a given stock ticker based on scraped article titles.

get_sentiment_dict(tickers)
Calculates and returns a dictionary of stock tickers mapped to their average sentiment values.

get_true_sentiment_dict(sentiment_dict)
Normalizes sentiment values for each stock ticker by subtracting the average sentiment across all tickers. This aims to take into account overall market sentiment.

portfolio_allocation(true_sentiment_dict)
Adjusts the portfolio allocation based on normalized sentiment values for each stock ticker.

calculate_strategy(tickers)
The main function of the file, perform sentiment analysis on financial articles and output a dictionary with stock ticker symbols as keys and corresponding percentages in the portfolio for each stock.

	API interaction - xAPIconnector.py
Python wrapper provided by XTB to improve the convenience of using the XTB API for trading purposes.

	API interaction - APIFunctions.py
Contains multiple functions that further simplify the interaction with the XTB API for the specific purposes of this bot.

APIClient() initializes the xAPIConnector API client, allowing users to interact with the trading platform.

loginCommand(userID, password, appName='') 
Authenticates the user with the provided credentials.

buy(...)
Executes a buy transaction with customizable parameters, returning responses from the trade transaction and its status query.

sell(...) 
Executes a sell transaction with customizable parameters, responding to the trade transaction and its status query.

get_stocks_value() 
Retrieves the total value of all stocks in the portfolio through the xAPIConnector API.

get_portfolio() 
Retrieves the current portfolio based on open trades, returning a dictionary with stock symbols as keys and corresponding nominal values.

get_stock_price(symbol) 
Fetches the current ask price for a given stock symbol from the xAPIConnector API.


	Executing the trading bot - main.py 
The main file of the program can be executed to adjust an account trading portfolio based on an output portfolio derived from sentiment analysis.

adjust_position(symbol)
Adjusts the position of a specific stock in the portfolio, considering the difference between the current and desired values. It determines whether to buy or sell the stock and, if applicable, calls the confirm_and_make_transaction function to execute the transaction.

confirm_and_make_transaction(symbol, volume, type)
Prompts the user for confirmation before executing a stock transaction. It prints a confirmation message and calls the appropriate buy or sell function from the xAPIConnector API based on user input.
adjust_portfolio(desired_portfolio)

This function adjusts the current portfolio based on the desired portfolio allocation, iterating through each symbol and calling the adjust_position function. The resulting list contains transactions made during the adjustment.

main()
The main function conducts the whole portfolio adjustment process by calling other functions, printing the list of transactions made, and displaying the current and desired portfolios.




