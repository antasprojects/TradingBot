from strategy import calculate_strategy
from APIFunctions import get_stock_price, get_portfolio, buy, sell
from inputs import tickers, Investment


# Get the exchange rate for GBP to USD
GBPUSD = get_stock_price("GBPUSD")

# Retrieve the current portfolio and calculate the desired portfolio based on sentiment analysis
current_portfolio = get_portfolio()
desired_portfolio = calculate_strategy(tickers)

def adjust_portfolio(desired_portfolio):
    """
    Adjust the current portfolio based on the desired portfolio allocation.

    Args:
        desired_portfolio (dict): The desired portfolio allocation.
        current_portfolio (dict): The current portfolio allocation.

    Returns:
        list: A list of transactions made during the portfolio adjustment.
    """
    transaction_list = []
    for symbol in desired_portfolio:
        transaction = adjust_position(symbol)
        transaction_list.append(transaction)
    return transaction_list
    
            
def adjust_position(symbol):

    """
    Adjust the position of a specific stock in the portfolio.

    Args:
        symbol (str): The stock symbol.

    Returns:
        str or None: A confirmation message if a transaction is made, otherwise None.
    """
    # 
    stock_key = symbol + ".US_9"

    if stock_key in current_portfolio:
        current_value = round(Investment * current_portfolio[stock_key] / 100 , 2)
    else:
        current_value = 0 

    desired_value = round(Investment * desired_portfolio[symbol] / 100 , 2)
    current_price = get_stock_price(stock_key)
    current_price = current_price / GBPUSD
    if current_value < desired_value:
        # Buy more of the stock
        volume = round((desired_value - current_value) / current_price, 0)
        if volume:
            transaction = confirm_and_make_transaction(symbol, volume, "buy")
            return transaction

    elif current_value > desired_value:
        # Sell some of the stock
        volume = round((current_value - desired_value) / current_price, 0)
        if volume:
            transaction = confirm_and_make_transaction(symbol, volume, "sell")
            return transaction

    return None


def confirm_and_make_transaction(symbol, volume, type):
    """
    Confirm and execute a stock transaction.

    Args:
        symbol (str): The stock symbol.
        volume (float): The volume of shares to buy or sell.
        transaction_type (str): The type of transaction ("buy" or "sell").

    Returns:
        str or None: A confirmation message if the transaction is confirmed, otherwise None.
    """
    while True:
        user_input = input(f"To adjust the portfolio, you have to {type} {volume} shares of {symbol}. Do you confirm the transaction? (y/n): ").lower()
        if user_input == 'y':
            # Make the transaction (replace this with your actual transaction logic)
            print(f"Transaction confirmed for {symbol} - {type} {volume} shares.")
            if type == "buy":
                buy(symbol + ".US_9", volume)
                return f"Transaction confirmed for {symbol} - {type} {volume} shares."
            elif type == "sell":
                sell(symbol + ".US_9", volume)
                return f"Transaction confirmed for {symbol} - {type} {volume} shares."

        elif user_input == 'n':
            print("Transaction canceled.")
            return
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")
            return


def main():
    """
    Main function to execute the portfolio adjustment based on sentiment analysis.
    """
    transations = adjust_portfolio(desired_portfolio)
    current_portfolio = get_portfolio()
    print("Portfolio has been adjusted, list of transactions made:")
    for transaction in transations:
        if transaction:
            print(transaction)
    print("Your current portfolio is: ")
    print(current_portfolio)
    print("The desired portfolio calculated is: ")
    print(desired_portfolio)
    return

main()