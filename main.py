#!/usr/bin/python3

# importing tempfile
import tempfile
# importing json
import json
# importing checks
from checksOnChecks.check_README import Checks
# import gitpython
try:
    import git
except ImportError:
    print("please install gitpython, use sudo pip3 install gitpython")
    print("see https://gitpython.readthedocs.io/en/stable/intro.html for more details")

# get checker api key and check if they are missing any checks
# if missing checks clone repo to check for basic mistakes

# makes a temporary directory and saves the github repo to it
with tempfile.TemporaryDirectory() as path:
    #open the json and load the repo
    with open("vars.json") as vars:
                variable = json.load(vars)
    repo = variable["repo"]
    # git clone the repo to the path
    print("getting Repo")
    git.Git(path).clone(repo)
    my_check = Checks()
    my_check.check_README(path)
    my_check.check_executable(path)