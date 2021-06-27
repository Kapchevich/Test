from pydantic import BaseModel

class Param():
    api_key = "43a4f174-4d35-4d54-94b9-7923b993a0ef"
    url_quotes = ("https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest")
    convert_param = "RUB"
    id_param = "1"
    param_quotes = {'id': f"{id_param}",
                "convert": f"{convert_param}",
                "aux": "num_market_pairs,cmc_rank,date_added,platform,max_supply,circulating_supply,total_supply",
                "skip_invalid": "false"}


class Status(BaseModel):
    timestamp: str
    error_code: int
    error_message: None
    elapsed: int
    credit_count: int
    notice: None


class Data(BaseModel):
    id: int
    name: str
    symbol: str
    slug: str
    num_market_pairs: int
    date_added: str
    max_supply: int
    circulating_supply: int
    total_supply: int
    platform: None
    cmc_rank: int
    last_updated: str


class Quote(BaseModel):
    price: int
    volume_24h: int
    percent_change_1h: int
    percent_change_24h: int
    percent_change_7d: int
    percent_change_30d: int
    percent_change_60d: int
    percent_change_90d:int
    market_cap: int
    last_updated: str

