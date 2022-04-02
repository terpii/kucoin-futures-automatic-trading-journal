import kucoin_futures

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
print(f'Loaded api password: {api_password}')
