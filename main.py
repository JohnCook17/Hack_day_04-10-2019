#!/usr/bin/python3

# importing tempfile
import tempfile
# importing json
import json
# importing checks
from checksOnChecks.check_README import Checks
# import gitpython
from checksOnChecks.auth_token import get_auth
from checksOnChecks.get_checks import find_failed_checks
from checksOnChecks.get_checks import get_correction_ids


import sys

try:
    import git
except ImportError:
    print("please install gitpython, use sudo pip3 install gitpython")
    print("see https://gitpython.readthedocs.io/en/stable/intro.html\
          for more details")

failed_check_list = []
# get checker api auth_token and check if they are missing any checks
authToken = get_auth(sys.argv[1], sys.argv[2], sys.argv[3])
failed_check_list = find_failed_checks(authToken, sys.argv[4])

# if missing checks clone repo to check for basic mistakes

# makes a temporary directory and saves the github repo to it
with tempfile.TemporaryDirectory() as path:
    # open the json and load the repo
    with open("vars.json") as vars:
        variable = json.load(vars)
    repo = variable["repo"]
    # git clone the repo to the path
    print("getting Repo")
    if failed_check_list:
        git.Git(path).clone(repo)
        my_check = Checks()
        my_check.check_README(path)
        my_check.check_executable(path)

print(failed_check_list)
if len(failed_check_list) == 1:
    print('You have {:d} task with missing requirement checks')
else if len(failed_check_list) > 1:
    print('You have {:d} tasks with missing requirement checks')
      .format(len(failed_check_list)))
commonMistakes = """      Common Mistakes you may have missed

                 Did you remember all the semicolons
                 or tabs depending on language?
                 Did you do you syntax checks (Betty, pep8, etc)?
                 Do you have the proper shebang?
                 Do you have the proper return?
                 Did you try other test cases?
                 Did you check your spelling?
                 Are you printing the required output?
                 Did you follow all the directions for this task?
                """
print(commonMistakes)
