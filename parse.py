import requests
import json
from pydantic import ValidationError
from schema import *


def get_coinmarket():
    headers = {
        'X-CMC_PRO_API_KEY': Param.api_key,
    }
    response = requests.get(Param.url_quotes, headers=headers, params=Param.param_quotes)
    return response


def get_json(param):
    response = get_coinmarket()
    data = response.json()
    return data[param]


def parse_json(data):
    j = json.dumps(data)
    return j


def valid(cls, data):
    try:
        parse = cls.parse_raw(data)
        return parse.json()
    except ValidationError as e:
        print(e.json())
