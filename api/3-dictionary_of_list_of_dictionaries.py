#!/usr/bin/python3
"""
Export API data to CSV format
Format: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
Filename: USER_ID.csv
all tasks from all employees
"""
import json
import requests
import sys


def get_employee_tasks(employeeId):
    """Get the tasks of an employee"""
    url = "https://jsonplaceholder.typicode.com/users/{}/todos"\
        .format(employeeId)
    response = requests.get(url)
    return response.json()


def get_employee_name(employeeId):
    """Get the name of an employee by adding the employeeId to the URL"""
    url = "https://jsonplaceholder.typicode.com/users/{}".format(employeeId)
    response = requests.get(url)
    return response.json().get("username")


def export_all_to_json():
    data_dict = {}

    # Fetch tasks for all employees and organize in the desired format
    for employeeId in range(1, 11):  # Assuming employee IDs range from 1 to 10
        tasks = get_employee_tasks(employeeId)
        employeeName = get_employee_name(employeeId)

        employee_data = []
        for task in tasks:
            task_data = {
                "username": employeeName,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            employee_data.append(task_data)

        data_dict[str(employeeId)] = employee_data

    json_data = json.dumps(data_dict)

    filename = "todo_all_employees.json"
    with open(filename, "w") as jsonfile:
        jsonfile.write(json_data)


if __name__ == "__main__":
    export_all_to_json()
