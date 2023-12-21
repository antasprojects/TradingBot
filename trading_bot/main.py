from strategy import main
from APIFunctions import get_stock_price, get_porfolio


Investment = 50000
#Inputs: 
#  - Money invested (GBP)
# Objectives:
#
# 1. Check the allocation of the current portfolio
# 2. Check the calculated desired portfolio according to the strategy (based on the sentiment)
# 3. Make the transactions required to achieve the desired portfolio distribution
current_portfolio = get_porfolio()

desired_portfolio = main()

print(current_portfolio)
print(desired_portfolio)

def adjust_portfolio(current_portfolio, desired_portfolio):

    for symbol in current_portfolio:
        value_difference = current_portfolio[symbol] - desired_portfolio[symbol]
        stock_price = get_stock_price(symbol)
        if value_difference > 0:
            x = 0
            

def adjust_position(symbol):
    current_value = round(Investment * current_portfolio[symbol] / 100 , 2)
    desired_value = round(Investment * desired_portfolio["AMZN"] / 100 , 2)
    current_price = get_stock_price(symbol)
    GBPUSD = get_stock_price("GBPUSD")
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

