import requests
import json
import os
os.system('cls')

#####################################
api_request = requests.get("https://api.coinmarketcap.com/v1/ticker/")
api = json.loads(api_request.content)


# my Portfolio
my_portfolio = [
     {

           "sym": "STEEM",
           "amount_owned": 3000,
           "price_paid_per": .80
      },

      {

           "sym": "XRP",
           "amount_owned": 5000,
           "price_paid_per": .20
      },

       {

           "sym": "XLM",
           "amount_owned": 2000,
           "price_paid_per": .10
      },


       {

           "sym": "EOS",
           "amount_owned": 1000,
           "price_paid_per": 2.00
      },
  ]
print("=========================")
for x in api:
    for coin in my_portfolio:
        if coin["sym"] == x["symbol"]:
            print(x["name"])
            print("${0:.2f}".format(float(x["price_usd"])))
            print("Rank:{0:.0f}".format(float(x["rank"])))
            print("==========================")
