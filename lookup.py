import requests
import json
import os
os.system('cls')
#########################################


api_request = requests.get( "https://api.coinmarketcap.com/v1/ticker/")
api = json.loads(api_request.content)

print(api)