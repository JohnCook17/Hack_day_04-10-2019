#!/usr/bin/pyton3
import os
import sys


def check_executable(filename=""):
    """ Tested with dummy files  but needs to be inplemented with
        filepath but checks for exec permissions"""
    line = 0
    with open(filename, "r") as foo:
        for line in foo:
            path_ok = os.access("fizzy2.py", os.X_OK)
            path_not_ok = os.access("ok.py", os.X_OK)

    except Exception as err:
        print(err)
    print("Check if file is executable:", path_ok)
    print("Check if file is executable:", path_not_ok)
