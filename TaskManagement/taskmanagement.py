#Task management system nested dictionary

#Information to search by Task ID, starting from Task ID 1
import easygui

task_id = {
    "Task1" : {

        "Task_ID" : "T1",
        "Title" : "Design Homepage",
        "Description" : "Create a mockup of the homepage",
        "Assignee" : "JSM",
        "Priority" : "3",
        "Status" : "In Progress",

    },

    "Task2" : {
        "Task_ID" : "T2",
        "Title" : "Implement Login Page",
        "Description" : "Create the Login page for the website",
        "Assignee" : "JSM",
        "Priority" : "3",
        "Status" : "Blocked",

    },

    "Task3" : {
        "Task_ID" : "T3",
        "Title" : "Fix Navigation Menu",
        "Description" : "Fix the navigation menu to be user friendly",
        
    }

}

def display_tasks(tasks):
    #Allows the user to select a task from choices.
    output = "" 
    tasks = []
    for titles in task_id:
        tasks.append(titles)

    msg = "What Task ID would you like to select?"

    title = "Task Choice"

    task_choice = easygui.buttonbox(msg, title, tasks)

    task_info = []

    for task_information in task_id[task_choice]:
        task_info.append(task_information)


#Menu to choose which task needs to be opened
def menu(tasks):
    while True:
        choice = easygui.buttonbox("Choose an action:", "Task Manager Menu", ["View All Tasks", "Edit task", "Exit"])
#Retrieve values of the selected task

#allow the user to select a task from the menu






