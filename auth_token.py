#!/usr/bin/python3
''' method to return the auth_token'''

import sys
import requests

if __name__ == "__main__":
    ''' 
    needs to eventually be turned to a method but this prints and returns the auth_token
    when the user enters parameters api_key, email, password, in that order
    '''
    authentication = requests.post("https://intranet.hbtn.io/users/auth_token.json", params={'api_key': sys.argv[1], 'email': sys.argv[2], 'password': sys.argv[3], 'scope': 'checker' })
    print(sys.argv[0], sys.argv[1], sys.argv[2], sys.argv[3])
    auth_dict = authentication.json()
    print(auth_dict.get('auth_token'))
    return auth_dict.get('auth_token')
