#!/usr/bin/pyton3
if __name__ == "__main__":

    import os
    import sys
    import json


    def check_executable():
        """ Tested with dummy files  but needs to be inplemented with 
        filepath but checks for exec permissions"""
    try:
         path_ok = os.access('ok.py', os.X_OK)
         path_not_ok = os.access('not_ok.py', os.X_OK)

    except IOError as err:
        print(err)
    print("Check if file is executable:", path_ok)
    print("Check if file is executable:", path_not_ok)
