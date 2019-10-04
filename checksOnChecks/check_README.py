#!/usr/bin/python3
if __name__ != "__main__":

    import json
    from os import path
    class Checks():
        def check_README(self, my_path):
            """ checks if the readme file is at least 100 char long 
            """
            with open("vars.json") as vars:
                variable = json.load(vars)
                repo = variable["repo"].split("/")[4].split(".")[0]
                print(repo)
            readme_path = my_path + "/" + repo + "/README.md"
            if path.exists(readme_path):
                with open(my_path + "/" + repo + "/README.md") as r:
                    if len(r.read()) < 100:
                        print("README.md does not exist or is not long enough.")
                        return 0
                    else:
                        print("README.md looks good, but can always be better.")
                        return 1
            else:
                print("README.md is missing")
                return 0