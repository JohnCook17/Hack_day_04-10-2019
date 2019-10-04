#!/usr/bin/python3
''' The get_checks module'''
import requests
auth = __import__('auth_token').get_auth


if __name__ == "__main__":
    auth_id = auth('593323cf3f7cfcb59ed1725f340eab58', '525@holbertonschool.com', 'Mbappe107')
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
            print(correction_id)
        """    correction_res = requests.get('https://intranet.hbtn.io/correction_requests/{}.json?auth_token={}'.format(correction_id, auth_id))
            check_list = correction_res.json().get('result_display').get('checks')
            print(check_list)
            for check in check_list:
                print(check)	
                if check.get('check_label') == "requirement" and check.get('passed') is False:
                    print("It's going in there")
                    failed_tasks['taskname'] = taskid
       
 		
        print(failed_tasks)
        return failed_tasks
       """

find_failed_checks()
