#!/usr/bin/python3
''' The get_checks module'''
import requests
auth = __import__('auth_token').get_auth


if __name__ == "__main__":
    auth_id = auth('f08b491db334657dc706e958b807c2c7', '682@holbertonschool.com', '3zPk&fkG6mAf')
    def find_failed_checks():
        """ Method that gets all the tasks with failed checks"""
        tasks = {};
        failed_tasks = {};
        req = requests.get('https://intranet.hbtn.io/projects/260.json?auth_token={}'.format(auth_id))
        for i in req.json().get('tasks'):
            if i.get('checker_available') is True :
                tasks[i.get('title')] = i.get('id')

        for taskname, taskid in tasks.items():
            req_correction = requests.post('https://intranet.hbtn.io/tasks/{}/start_correction.json?auth_token={}'.format(taskid, auth_id))
            correction_id = (req_correction.json().get('id'))
            correction_res = requests.get('https://intranet.hbtn.io/correction_requests/{}.json?auth_token={}'.format(correction_id, auth_id))
            check_list = correction_res.json().get('result_display').get('checks')
            for check in check_list:
                if check.get('check_label') == "requirement" and check.get('passed') is False:
                    failed_tasks['taskname'] = taskid

        print(failed_tasks)
        return failed_tasks

find_failed_checks()
