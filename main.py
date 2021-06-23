import requests

api_key = "43a4f174-4d35-4d54-94b9-7923b993a0ef"
url_quotes = ("https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest")
url_key = ("https://pro-api.coinmarketcap.com/v1/key/info")
param_quotes = {'id': "1", "convert": "RUB", "aux": "num_market_pairs,cmc_rank,date_added,tags,platform,max_supply,circulating_supply,total_supply", "skip_invalid": "false"}
param_key = {}

def get_coinmarket(url, param):
    headers = {
        'X-CMC_PRO_API_KEY': api_key,
    }

    response = requests.get(url, headers=headers, params=param)
    response_json = response.json()
    code = response.status_code
    print(response_json)
    return code


if get_coinmarket(url_key, param_key) == 200:
    print("KeyTest is PASS")
else:
    print("KeyTest FILED")

if get_coinmarket(url_quotes, param_quotes) == 200:
    print("QuotesTest is PASS")
else:
    print("QuotesTest FILED")