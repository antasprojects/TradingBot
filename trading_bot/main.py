from strategy import calculate_strategy
from APIFunctions import get_stock_price, get_porfolio
from inputs import tickers, Investment
GBPUSD = get_stock_price("GBPUSD")

# 1. Check the allocation of the current portfolio
# 2. Check the calculated desired portfolio according to the strategy (based on the sentiment)
# 3. Make the transactions required to achieve the desired portfolio distribution


def adjust_portfolio(current_portfolio, desired_portfolio):
    for symbol in desired_portfolio:
        adjust_position(symbol)
            
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
        quantity_to_adjust = round((desired_value - current_value) / current_price, 0)
        transaction_type = f"Buy {quantity_to_adjust} shares of {symbol}"
    elif current_value > desired_value:
        # Sell some of the stock
        quantity_to_adjust = round((current_value - desired_value) / current_price, 0)
        transaction_type = f"Sell {quantity_to_adjust} shares of {symbol}"

    return transaction_type

current_portfolio = get_porfolio()
desired_portfolio = calculate_strategy(tickers)

print(current_portfolio)
print(desired_portfolio)

print(adjust_portfolio(current_portfolio, desired_portfolio))