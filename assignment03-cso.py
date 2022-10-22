import requests
import json

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"

def get_data(table):
    begin_url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
    end_url = "/JSON-stat/2.0/en"
    search_url = begin_url + table + end_url
    response = requests.get(search_url)
    with open ("cso.json", "wt") as fp:
        print(json.dumps(response.json()), file = fp)
    return response.json()

get_data("FIQ02")