#!/usr/bin/python3

import requests

task_info = {}


def find_failed_checks(auth_id, proj_num, correction_ids=[]):
    """ Method that gets all the tasks with failed checks"""
    failed_tasks = {}
    list_of_dicts = []
    if not correction_ids:
        correction_ids = get_correction_ids(auth_id, correction_ids, task_info, proj_num)
        while(1):
            for correction_id in correction_ids:
                correction_res = requests.get('https://intranet.hbtn.io/correction_requests/{}.json?auth_token={}'.format(correction_id, auth_id))
                check_list = correction_res.json().get('result_display').get('checks')
                print("Working")
                print("Still Working")

                if check_list is not []:
                    for check in check_list:
                        if check.get('check_label') == "requirement" and check.get('passed') is False:
                            failed_tasks[check.get('title')] = check.get('passed')
            if failed_tasks:
                list_of_dicts.append(failed_tasks)
            failed_tasks = {}
            if correction_res.json().get('status') == 'Done':
                break
    return list_of_dicts


def get_correction_ids(auth_id, correction_ids, task_info, proj_num):
    tasks = {}
    req = requests.get('https://intranet.hbtn.io/projects/{}.json?auth_token={}'.format(proj_num, auth_id))
    for i in req.json().get('tasks'):
        if i.get('checker_available') is True:
            tasks[i.get('title')] = i.get('id')
    for taskname, taskid in tasks.items():
        req_correction = requests.post('https://intranet.hbtn.io/tasks/{}/start_correction.json?auth_token={}'.format(taskid, auth_id))
        correction_id = (req_correction.json().get('id'))
        correction_ids.append(correction_id)
        task_info[taskname] = taskid
    return correction_ids
