#!/usr/bin/python3
if __name__ != "__main__":
    
    import os
    import sys
    import json
    import json
    from os import path


    class Checks():
        def check_README(self, my_path):
            """ checks if the readme file is at least 100 char long 
            """
            with open("vars.json") as vars:
                variable = json.load(vars)
                repo = variable["repo"].split("/")[4].split(".")[0]
                subfolder = variable["subfolder"]
                print(repo)
                print(subfolder)
            if not subfolder:
                readme_path = my_path + "/" + repo + "/README.md"
            else:
                readme_path = my_path + "/" + repo + "/" + subfolder + "/README.md"
                if path.exists(readme_path):
                    print(readme_path)
                    with open(readme_path) as r:
                        readme = r.read()
                        print(readme)
                        if len(readme) < 100:
                            print("README.md is not long enough.")
                            return 0
                        else:
                            print("README.md looks good, but can always be better.")
                            return 1
                else:
                    print("README.md is missing")
                    return 0


        def check_executable(self, my_path):
            """ Tested with dummy files  but needs to be implemented with 
            filepath but checks for exec permissions"""
            with open("vars.json") as vars:
                variable = json.load(vars)
                repo = variable["repo"].split("/")[4].split(".")[0]
                subfolder = variable["subfolder"]
                print(repo)
                print(subfolder)
            if not subfolder:
                file_path = my_path + "/" + repo
            else:
                file_path = my_path + "/" + repo + "/" + subfolder
            for dir_name, subdirlist, filelist in os.walk(file_path):
                print("working in %s" % dir_name)
                for file_name in filelist:
                    print(filelist)
                    print("=============================")
                    print(file_name)
                    try:
                        path_ok = os.access(file_name, os.X_OK)
                    except IOError as err:
                        print(err)
                    print("Check if %s file is executable:"% file_name, path_ok)

