from strategy import calculate_strategy
from APIFunctions import get_stock_price, get_porfolio, buy, sell
from inputs import tickers, Investment


GBPUSD = get_stock_price("GBPUSD")
current_portfolio = get_porfolio()
desired_portfolio = calculate_strategy(tickers)


def adjust_portfolio(desired_portfolio):
    transaction_list = []
    for symbol in desired_portfolio:
        transaction = adjust_position(symbol)
        transaction_list.append(transaction)
    return transaction_list
    
            
def adjust_position(symbol):

    if symbol + ".US_9" in current_portfolio:
        current_value = round(Investment * current_portfolio[symbol + ".US_9"] / 100 , 2)
    else:
        current_value = 0 

    desired_value = round(Investment * desired_portfolio[symbol] / 100 , 2)
    current_price = get_stock_price(symbol + ".US_9")
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

    return 


def confirm_and_make_transaction(symbol, volume, type):
     while True:
        clear_console()
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
    transations = adjust_portfolio(desired_portfolio)
    current_portfolio = get_porfolio()
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