import json
import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth
import base64

class Credentials:
    consumer_key = '77bgGpmlOxlgJu6oEXhEgUgnu0j2WYxA'
    consumer_secret = 'viM8ejHgtEmtPTHd'
    passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'


class MpesaAccessToken:
    tokens = requests.get(Credentials.api_URL, auth=HTTPBasicAuth(Credentials.consumer_key, Credentials.consumer_secret))
    access_token = json.loads(tokens.text)
    validated_access_token = access_token["access_token"]


class MpesaPassword:
    pay_time = datetime.now().strftime('%Y%m%d%H%M%S')
    short_code = "174379"
    OffSetValue = '0'
    passkey = Credentials.passkey

    encodes = short_code + passkey + pay_time

    encoded = base64.b64encode(encodes.encode())

    decoded = encoded.decode('utf-8')