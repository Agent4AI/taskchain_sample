import requests

from requests.auth import HTTPBasicAuth

def get_data_record(orderId, metadata):
    auth = HTTPBasicAuth(metadata['shipstation_api_key'], metadata['shipstation_api_secret'])


    HOST="https://ssapi.shipstation.com"

    r = requests.get(HOST + "/orders?orderNumber=" + orderId, auth=auth)

    return r.json()