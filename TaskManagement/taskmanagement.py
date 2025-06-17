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

    }

}

#Menu to choose which task needs to be opened
def menu():

    tasks = {
        "Select Task" : select_task
    }

#Retrieve values of the selected task

    get_input ="Y"  

#allow the user to select a task from the menu

    while get_input == "Y":
        msg = "Please select a Task ID to view"
        title = "Task ID Choices"
        choices = list(task_id)

    for items in tasks:
        choices.append(items)
    
    task_selection = easygui.buttonbox(msg, title, choices)


def select_task():
    #Allows the user to select a task from choices.
    output = ""
    tasks = []
    for titles in task_id:
        tasks.append(titles)

    msg = "What Task ID would you like to select?"

    title = "Task Choice"

    task_choice = easygui.buttonbox(msg, title, tasks)

menu()
    


