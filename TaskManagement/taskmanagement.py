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
    """Prints the selection of tasks and their details including new
      tasks that have been added and edited tasks"""
    output = ""

    for task_title in task_id:
        output += f"\n{task_title}\n"

        for key, value in task_id[task_title].items():
            output += f"{key}: {value}\n" #looks through the task
            #dictionary 

    easygui.msgbox(output, "All Tasks") #message box will display all
    #tasks and details
    return "Y"

def search_task():
    choice = easygui.buttonbox("Search by:", "Search Options", ["Task ID", 
                                                                "Assignee"])

    if choice == "Task ID":
        task_name = easygui.enterbox("Enter the task ID (e.g Task1):", "Search"
        " for a task")
         #asks the user for input of
        #searching a task by name

        if task_name in task_id: 
            task = task_id[task_name] #checks if the entered
            #task name exists in the task_id dict
            message = ""
            for key, value in task.items(): #looks through the task
                #dictionary
            
                message += f"{key}: {value}\n"
                 #finds the key inputted by the user in the search box

            easygui.msgbox(message, f"Details for {task_name}") 
            #runs through the key in dictionary and provides a msgbox 
            # of the items
        else:   
            easygui.msgbox("Task not found. Please input a valid Task ID")
             #invalid task id was entered, will prompt the user
             #to input a valid task Id

    elif choice == "Assignee":
        name = easygui.enterbox("Enter the assignee's 3 letter code (e.g JSM):"
                                , "Search by Assignee") #allows the user
        #to search by an assignee rather than

    

#search_task()  called from within menu    

def display_tasks():
    #Allows the user to select a task from choices.
    output = "" 
    tasks = [task_id]
    for titles in task_id:
        tasks.append(titles)

    msg = "What Task ID would you like to select?"

    title = "Task Choice"

    task_choice = easygui.buttonbox(msg, title, tasks)

    task_info = []

    for task_information in task_id[task_choice]:
        task_info.append(task_information)

def generatetaskid():
    """Generates a new task ID based on the number of existing tasks"""
    task_count = len(task_id)
    new_task_id = f"T{task_count + 1}"
    return new_task_id #instead of the user having to input a task ID,
#this function will add a new Task id based on the number of existing
#tasks in the dictionary

def progress_report():
    """ generates a report of the tasks progress including 
    the number of tasks completed, the number of tasks in progress,
    the number of tasks blocked, and the number of tasks not yet started"""

def add_task():
    confirm_choices = ["Yes", "No"]
    task_information = ["Title", "Description", "Assignee", "Priority", 
                        "Status"]
    
    msg = "Enter new task title:"
    title = "New Task Title"

    new_task_name = easygui.enterbox(msg, title)

    if new_task_name == None or new_task_name == "":
        return

    new_task_id = generatetaskid()
    task_id[new_task_name] = {"Task_ID": new_task_id}
    output = f"Task_ID: {new_task_id}\n"

    for new_task_information in task_information:
        msg = f"Enter the {new_task_information} for {new_task_name}"
        title = f"{new_task_name} {new_task_information}"

        new_task_info = easygui.enterbox(msg, title)

        if new_task_info == None or new_task_info == "":
            easygui.msgbox("Cancelling procedure")
            del task_id[new_task_name]
            return

        output += f"{new_task_information}: {new_task_info}\n"
        task_id[new_task_name][new_task_information] = new_task_info

    msg = "Please double check if the task details entered are correct"
    title = "Task Confirmation"
    easygui.msgbox(output, title)

def edit_task():

    output = ""
    task_titles = []
    for titles in task_id:
        task_titles.append(titles)

    msg = "What task would you edit the details of?"
    title = "TASK CHOICE"

    task_choice = easygui.buttonbox(msg, title, task_titles)

    task_info = []

    for task_information in task_id[task_choice]:
        task_info.append(task_information)

    msg = f"What detail of {task_choice} would you like to edit"
    title = "TASK CHOICE"

    edit_choice = easygui.buttonbox(msg, title, task_info)

    msg = f"Enter the new {edit_choice} for {task_choice}"
    title = f"ENTER UPDATED TASK INFORMATION"

    #Line of code which is editing the game value
    task_id[task_choice][edit_choice] = easygui.enterbox(msg, title) 
        
#Menu to choose which task needs to be opened
def menu():
    while True:
        selection = easygui.buttonbox("Choose an action:", "Task Manager Menu",
                                       ["View All Tasks", "Edit Task", "Exit", 
                                        "Search Task", "Add Task"])
        #displays menu options for the user to choose from

        if selection == "View All Tasks": #if the user selects view
            #all tasks, the print_all_tasks function is called.
            print_all_tasks()
        elif selection == "Exit": #if the user selects exit,
            #the program will end.
            break
        elif selection == "Search Task": #if the user selects search
            #task, the search_task function is called.
            search_task()
        elif selection == "Add Task": #if the user selects add task,
            #the add task function is called.
            add_task()
        elif selection == "Edit Task": #if the user selects edit task,
            # the edit_task function is called.
            edit_task()
            

menu()



