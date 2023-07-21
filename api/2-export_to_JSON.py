#!/usr/bin/python3
"""
Export API data to CSV format
Format: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
Filename: USER_ID.csv
"""
import csv
import json
import requests
import sys
import urllib.request


def get_employee_tasks(employeeId):
    """Get the tasks of an employee"""
    url = "https://jsonplaceholder.typicode.com/"
    url += "users/{}/todos".format(employeeId)
    response = requests.get(url)
    return response.json()


def get_employee_name(employeeId):
    """Get the name of an employee by adding the employeeId to the URL"""
    url = "https://jsonplaceholder.typicode.com/"
    url += "users/{}".format(employeeId)
    response = requests.get(url)
    return response.json().get("username")


def get_completed_tasks(tasks):
    """
    Get the completed tasks of an employee by adding tasks to a list
    if the task is completed
    """
    completed_tasks = []
    for task in tasks:
        if task.get("completed"):
            completed_tasks.append(task)
    return completed_tasks


def print_employee_tasks(employeeName, completedTasks, totalTasks):
    """Print the tasks of an employee"""
    print("Employee {} is done with tasks({}/{}):"
          .format(employeeName, len(completedTasks), totalTasks))
    for task in completedTasks:
        print("\t {}".format(task.get("title")))


def export_to_json(employeeId, tasks):
    """Export the tasks of an employee to JSON format"""
    employeeName = get_employee_name(employeeId)
    employeeId = str(employeeId)
    employee = {employeeId: []}
    for task in tasks:
        taskDict = {"task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": employeeName}
        employee[employeeId].append(taskDict)
    with open("{}.json".format(employeeId), "w") as jsonfile:
        json.dump(employee, jsonfile)


if __name__ == "__main__":
    employeeId = sys.argv[1]
    tasks = get_employee_tasks(employeeId)
    employeeName = get_employee_name(employeeId)
    completedTasks = get_completed_tasks(tasks)
    print_employee_tasks(employeeName, completedTasks, len(tasks))
