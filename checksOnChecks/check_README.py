#!/usr/bin/python3
if __name__ == "__main__":

    import json
    def check_README():
        """ needs to be imported into the main file, checks if the readme file
        is at least 1 char long 
        """
        with open("vars.json") as vars:
            variable = json.load(vars)
            repo = variable["repo"].split("/")[4].split(".")[0]
        with open(variable["path"] + "/" + repo + "/README.md") as r:
            if len(r.read()) < 0:
                print("README.md does not exist or is not long enough.")
            else:
                print("README.md looks good, but can always be better.")
