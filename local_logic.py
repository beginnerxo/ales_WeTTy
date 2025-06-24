'''
User should be able to 

Add 

View 

Delete/ 

And / complete tasks

'''

tasks = []
completed_task= []



def add(task_to_add: str):
    tasks.append(task_to_add)
    return("Task Added Succeffully")
   
    

def view_all():
    return [f"{number + 1}: {task}" for number, task in enumerate(tasks)]

        

def delete(task_to_delete):
    for task_to_delete in tasks:
        tasks.remove(task_to_delete)
        return("Task removed successfully")
    return("Task Not Found")


def check_if_exists(task_to_check):
    if task_to_check in tasks:
        return f"'{task_to_check}' exists"
    else:
        return f"'{task_to_check}' does not exist"

            


def complete(task_to_complete):
    if task_to_complete.casefold() in tasks:
        completed_task.append[task_to_complete]
        tasks.remove(task_to_complete)
        return("Task Marked as complete")
    return ("Task Not Found")
    
    
    


view_all()