#!/usr/bin/python3
"""
Define 3 functions to gather data from an API
Accept integer as parameter, which is the employee ID
Display on the standard output the employee TO DO list progress
in provided format
"""
import requests
import sys


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
    return response.json().get("name")


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


if __name__ == "__main__":
    employeeId = sys.argv[1]
    tasks = get_employee_tasks(employeeId)
    employeeName = get_employee_name(employeeId)
    completedTasks = get_completed_tasks(tasks)
    print_employee_tasks(employeeName, completedTasks, len(tasks))
