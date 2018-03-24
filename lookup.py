import requests
 import json
 import os
 os.system('cls')

#####################################
 api_request = requests.get("https"://api.coinmarketcap.com/v1/ticker/")
 for x in api:
	for coin in currencies:
	    if coin == x["symbol"]:
	       print(x["name"])
         print(x["price_usd"])
         print(x["rank"])
         print("${0:.2f}".format(float(x["price_usd"])))
	       print("Rank:{0:.0f}".format(float(x["rank"])))
	       print("==========================")
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         ####################################################################################
         	       
1
3
6
29
Bitcoin
$8516.86
Rank:1
==========================
Ripple
$0.64
Rank:3
==========================
EOS
$6.78
Rank:6
==========================
Steem
$1.99
Rank:29
==========================
