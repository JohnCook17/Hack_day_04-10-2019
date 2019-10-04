#!/usr/bin/python3

# importing os
import os
# import gitpython
try:
    import git
except ImportError:
    print("please install gitpython, use sudo pip3 install gitpython")
    print("see https://gitpython.readthedocs.io/en/stable/intro.html for more details")

# get checker api key and check if they are missing any checks
# if missing checks clone repo to check for basic mistakes

# path and repo below, should probably move to json file

path = "/mnt/c/dev/test_repo"
repo = "https://github.com/JohnCook17/holbertonschool-zero_day.git"


# make path and git clone the repo to the path
try:
    os.mkdir(path)
except OSError:
    print("Creation of the directory %s failed" % path)
else:
    print("Successfully created the directory %s" % path)

git.Git(path).clone(repo)

