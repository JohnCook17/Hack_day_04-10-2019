#!/usr/bin/python3
import requests
auth = __import__('auth_token').get_auth


if __name__ == "__main__":
    auth_id = auth('f08b491db334657dc706e958b807c2c7', '682@holbertonschool.com', '3zPk&fkG6mAf')
    def find_project_name():
        """ Method that gets the project name"""
        tasks = {};
        failed_tasks = {};
        req = requests.get('https://intranet.hbtn.io/projects/260.json?auth_token={}'.format(auth_id))
        name = req.json.get('name')
        return name
