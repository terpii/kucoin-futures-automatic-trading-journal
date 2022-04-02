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

#parse ids
order_ids = []
for order in order_history:
    order_ids.insert(-1 ,order['id'])


with open(trading_journal_location) as f:
    trading_journal_content = f.readlines()

# check if id is in file and add it to new_ids
new_ids = []
for id in order_ids:
    if id in trading_journal_content:
        continue
    else:
        new_ids.insert(-1, id)


# Get info about the orders
orders_info = []
for id in new_ids:
    id_info = client_trade.get_order_details(id)
    
    market = id_info['symbol']#currency pair
    order_type = id_info['type']
    order_side = id_info['side']#buy/sell
    leverage = id_info['leverage']
    quantity = id_info['size']
    value = id_info['filledValue']
    time = datetime.datetime.fromtimestamp(id_info['orderTime']/1000.0)
    used_currency = id_info['settleCurrency']

    
