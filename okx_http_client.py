from .config import OKXConfig
from .constant import *

import datetime, hmac, base64, requests, json

class OKXHttpClient:
    def __init__(self):
        self.FLAG = OKXConfig.FLAG
        self.API_KEY = OKXConfig.API_KEY
        self.SECRET_KEY = OKXConfig.SECRET_KEY
        self.PASSPHRASE = OKXConfig.PASSPHRASE
        self.CLIENT_URL = CLIENT_URL

    def _request(self, method, request_path, params):
        if method == GET:
            request_path = request_path + parse_params_to_str(params=params)
        timestamp = get_timestamp()
        body = json.dumps(params) if method == POST else ""
        sign = signature(timestamp, method, request_path, str(body), self.SECRET_KEY)
        header = get_header(api_key=self.API_KEY, sign=sign, timestamp=timestamp, passphrase=self.PASSPHRASE, flag=self.FLAG)
        print(self.CLIENT_URL+request_path)
        resp = requests.get(url=self.CLIENT_URL+request_path, params=params, headers=header, data=body)

        if resp.status_code != 200:
            print('request failed, msg: ', resp.json())
        return resp.json()
    
    def request_without_params(self, method, request_path):
        return self._request(method, request_path, {})

    def request_with_params(self, method, request_path, params):
        return self._request(method, request_path, params)

def parse_params_to_str(params):
    url = '?'
    for key, value in params.items():
        url = url + str(key) + '=' + str(value) + '&'
    print('url:',url)
    return url[0:-1]

def get_timestamp():
    now = datetime.datetime.utcnow()
    t = now.isoformat("T", "milliseconds")
    return t + "Z"

def get_header(api_key, sign, timestamp, passphrase, flag):
    header = dict()
    header[CONTENT_TYPE] = APPLICATION_JSON
    header[OK_ACCESS_KEY] = api_key
    header[OK_ACCESS_SIGN] = sign
    header[OK_ACCESS_TIMESTAMP] = str(timestamp)
    header[OK_ACCESS_PASSPHRASE] = passphrase
    header[SIMILATED_TRADING_SIGN] = flag
    print('header: ',header)
    return header

def signature(timestamp, method, request_path, body, secret_key):
    message = str(timestamp) + str.upper(method) + request_path + body 
    mac = hmac.new(bytes(secret_key, encoding='utf8'), bytes(message, encoding='utf-8'), digestmod='sha256')
    d = mac.digest()
    return base64.b64encode(d)
