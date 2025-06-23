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
        "Status" : "In Progress"

    },

    "Task2" : {
        "Task_ID" : "T2",
        "Title" : "Implement Login Page",
        "Description" : "Create the Login page for the website",
        "Assignee" : "JSM",
        "Priority" : "3",
        "Status" : "Blocked"

    },

    "Task3" : {
        "Task_ID" : "T3",
        "Title" : "Fix Navigation Menu",
        "Description" : "Fix the navigation menu to be user friendly",
        "Assignee" : "None",
        "Priority" : "1",
        "Status" : "Not Started"
        
    },

    "Task4" : {
        "Task_ID" : "T4",
        "Title" : "Add payment processing",
        "Description" : "Implement payment processing for the website",
        "Assignee" : "JLO",
        "Priority" : "2",
        "Status" : "In Progress"

    },

    "Task5" : {
        "Task_ID" : "T5",
        "Title" : "Create and About Us page",
        "Description" : "Create a page with information about the company",
        "Assignee" : "BDI",
        "Priority" : "1",
        "Status" : "Blocked"
    }
   
}

def print_all_tasks():
    """Prints the selection of tasks and their details"""
    output = ""

    for task_title in task_id:
        output += f"\n{task_title}\n"

        for key, value in task_id[task_title].items():
            output += f"{key}: {value}\n"

    easygui.msgbox(output, "All Tasks")
    return "Y"



def show_menu():        
    """Displays menu options for the user"""

    options = {
        #"Add Task": add_task,
        #"Remove Task": remove_task,
        #"Search Task": search_task,
        #"Edit Task": edit_task,
        "Print All Tasks": print_all_tasks,
        #"Exit": exit_tasks

    }

    get_input = "Y"

    while get_input == "Y":
        msg = "What would you like to do?"
        title = "Task Manager Application"
        choices = []

        for items in options:
            choices.append(items)

        selection = easygui.buttonbox(msg, title, choices)

        get_input = options[selection]()
    
show_menu()

"""
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

"""




