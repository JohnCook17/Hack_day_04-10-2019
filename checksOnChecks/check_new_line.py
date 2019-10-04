#!/usr/bin/python3
import sys

if __name__ == "__main__":

    def check_new_line():
        """ check for new line,  
        """
        with open("sys.argv[1]","r") as f:
            counter = 0
            while f.readline():
                counter += 1
        with open("sys.argv[1]","r") as foo:
            idx = 0
            while idx < counter:
                #if "\n" in foo.readline():
                 #   print("found newline")
                #else:
                idx += 1
            if idx == counter:
               if "\n" in foo.readline():
                   print("We've found the newline")
               else:
                   print("No new line found, you're all clear")
check_new_line()
