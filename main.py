#!/usr/bin/python3

#importing os
import os
#import gitpython
try:
    import git
except ImportError:
    print("please install gitpython, use sudo pip3 install gitpython")
    print("see https://gitpython.readthedocs.io/en/stable/intro.html for more details")

path = "/mnt/c/dev/test_repo"
repo = "https://github.com/JohnCook17/holbertonschool-zero_day.git"

try:
    os.mkdir(path)
except OSError:
    print("Creation of the directory %s failed" % path)
else:
    print("Successfully created the directory %s" % path)

git.Git(path).clone(repo)
