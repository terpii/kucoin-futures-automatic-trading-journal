# Kucoin futures automatic trading journal

This is a work-in-progress python script that can help traders analyse their profits, losses, and overall just understand what they are trading

## Usage
Simply run the python file after every trade and it will append the new info to the trading journal file

## Installation
``git clone https://github.com/terpii/kucoin-futures-automatic-trading-journal.git`` or download the zip file and unpack it

``cd kucoin-futures-automatic-trading-journal``

``python3 -m pip install kucoin_futures``

Now you will need to create an api access
- Go to https://futures.kucoin.com/api/create
- Write down your api password in the api_password
- It only needs the General permission
- Continue the steps and write down the api key in the api_key file and the secret api key into the api_key_secret file
Installation Finished! Now run it using ``python3 kucoin-futures-automatic-trading-journal.py``

## Todo
- Figure out what order values are
- Calculate profits/losses and other stats
