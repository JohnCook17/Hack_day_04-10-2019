#!/usr/bin/python3
''' The get_checks module'''
import requests
auth = __import__('auth_token').get_auth


if __name__ == "__main__":
    auth_id = auth('90aa475f9abd5d5dcdca03e44b8cb900', '655@holbertonschool.com', '92AntalopeRun')
    correction_ids = []
    task_info = {}
    def find_failed_checks():
        """ Method that gets all the tasks with failed checks"""
        #below
        failed_tasks = {}
        if not correction_ids:
            get_correction_ids()
        while(1):
            for correction_id in correction_ids:
                    correction_res = requests.get('https://intranet.hbtn.io/correction_requests/{}.json?auth_token={}'.format(correction_id, auth_id))
                    check_list = correction_res.json().get('result_display').get('checks')
                    print("Working")
                    print("Still Working")
                    for check in check_list:
                        if check.get('check_label') == "requirement" and check.get('passed') == False:
                            failed_tasks[check.get('title')] = check.get('passed')
            if correction_res.json().get('status') == 'Done':
                break
        print(failed_tasks)
        return failed_tasks

    def get_correction_ids():
        tasks = {}
        req = requests.get('https://intranet.hbtn.io/projects/293.json?auth_token={}'.format(auth_id))
        for i in req.json().get('tasks'):
            if i.get('checker_available') is True :
                tasks[i.get('title')] = i.get('id')
        for taskname, taskid in tasks.items():
            req_correction = requests.post('https://intranet.hbtn.io/tasks/{}/start_correction.json?auth_token={}'.format(taskid, auth_id))
            correction_id = (req_correction.json().get('id'))
            correction_ids.append(correction_id)
            task_info[taskname] = taskid

 


find_failed_checks()
