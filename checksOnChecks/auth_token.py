#!/usr/bin/python3
''' method to return the auth_token'''

import sys
import requests


def get_auth(api_key, email, password):
    authentication = requests.post("https://intranet.hbtn.io/users/auth_token.json", params={'api_key': api_key, 'email': email, 'password': password, 'scope': 'checker' })

    auth_dict = authentication.json()
    return auth_dict.get('auth_token')
