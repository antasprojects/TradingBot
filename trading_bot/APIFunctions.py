from xAPIConnector import APIClient, loginCommand, baseCommand


userId = 15468026
password = "Dupadupa1!"

client = APIClient()


loginCommand(userId, password, appName='')
loginResponse = client.execute(loginCommand(userId=userId, password=password))

def buy(symbol, volume, customComment="", price=10000, cmd=0, expiration=0, order=0, sl=0, tp=0, type=0):
    """
    Execute a buy transaction through the xAPIConnector API.

    Parameters:
    - symbol (str): The trading symbol for the transaction.
    - volume (float): The volume of the transaction.
    - customComment (str, optional): Custom comment for the transaction. Default is an empty string.
    - price (float, optional): The price of the transaction. Default is 10000.
    - cmd (int, optional): The command for the transaction. Default is 0.
    - expiration (int, optional): The expiration time for the transaction. Default is 0.
    - order (int, optional): The order for the transaction. Default is 0.
    - sl (float, optional): The stop-loss value for the transaction. Default is 0.
    - tp (float, optional): The take-profit value for the transaction. Default is 0.
    - type (int, optional): The type of transaction. Default is 0.

    Returns:
    tuple: A tuple containing two elements:
        - tradeTransactionResponse (dict): Response from the executed trade transaction.
        - tradeTransactionStatusResponse (dict): Response from the trade transaction status query.
    """
    arguments = {
        "tradeTransInfo": {
            "cmd": cmd,
            "customComment": customComment,
            "expiration": expiration,
            "order": order,
            "price": price,
            "sl": sl,
            "tp": tp,
            "symbol": symbol,
            "type": type,
            "volume": volume
        }
    }
    tradeTransactionResponse = client.execute(baseCommand("tradeTransaction", arguments))

    status_arguments = {
        "order": tradeTransactionResponse["returnData"]['order']
    }

    tradeTransactionStatusResponse = client.execute(baseCommand("tradeTransactionStatus", status_arguments))

    return tradeTransactionResponse, tradeTransactionStatusResponse
