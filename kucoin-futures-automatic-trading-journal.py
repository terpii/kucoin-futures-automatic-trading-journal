import kucoin_futures
import datetime

print('Successfully started kucoin futures trading journal\n')

def open_file(filename):
    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content][0]#Remove \n and stuff just incase
    return content

#Load api keys
api_key = open_file('api_key')
api_key_secret = open_file('api_key_secret')
api_password = open_file('api_password')

print(f'Loaded api keys:\napi_key: {api_key}\napi_key_priv: {api_key_secret}')
print(f'Loaded api password: {api_password}\n')

#Trading journal file location
trading_journal_location = 'tradingjournal'



#Get balance
from kucoin_futures.client import User

client_user = User(api_key, api_key_secret, api_password)
account_overview = client_user.get_account_overview(currency='USDT')

balance = account_overview["accountEquity"]

print(f'Current balance = {balance}')

#Get recent orders
from kucoin_futures.client import Trade

client_trade = Trade(key=api_key, secret=api_key_secret, passphrase=api_password, is_sandbox=False, url='https://api-futures.kucoin.com')

order_history = client_trade.get_24h_done_order()
 
# We will now iterate through every order and save the ones that aren't 
with open(trading_journal_location, 'r') as f:
    trading_journal_content = f.read()


# Get info about the orders
orders_string = ""
for order in order_history:
    order_id = order['id']

    if order_id in trading_journal_content:#if we already have it added, we skip
        continue
    
    
    order_side = order['side']#buy/sell
    order_type = order['type']#market/limit
    time = datetime.datetime.fromtimestamp(order['updatedAt']/1000.0)
    symbol = order['symbol']
    currency = order['settleCurrency']
    leverage = order['leverage']

    if order_side == 'sell':
        action = 'Sold'
    else:#buy order
        action = 'Bought'
    
    if order_type == 'market':
        volume = order['size']#in USDT
        price = order['stopPrice']#in USDT
    else:#type: limit
        price = order['price']
        volume = order['size']


    final_string = f"""
{order_id}:
{action} {volume} {currency} of {symbol} at the price of {price}
Type: {order_type}
Time: {time}
Leverage: {leverage}
"""

    orders_string = f'{orders_string}{final_string}\n'

# Put it all together in the file



date = datetime.datetime.now()

out_string = f"""
--------------------------------------
Time: {date}
Balance at time: {balance}

Trades:
{orders_string}
--------------------------------------

"""

f = open(trading_journal_location, 'w')
f.write(out_string + trading_journal_content)
f.close()

print('Finished! Check the journal file for results')