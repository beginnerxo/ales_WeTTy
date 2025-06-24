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
    tasks.append({"text":task_to_add, "done": False})
    return("Task Added Succeffully")
   
    

def view_all():
    return tasks

        
def delete(task_text):
    for task in tasks:
        if task["text"] == task_text:
            tasks.remove(task)
            return f"Deleted '{task_text}'"
    return f"Task '{task_text}' not found"



def check_if_exists(task_to_check):
    if task_to_check in tasks:
        return f"'{task_to_check}' exists"
    else:
        return f"'{task_to_check}' does not exist"

            


def complete(task_to_complete):
    for task in tasks:
        if task["text"] == task_to_complete:
            task["done"] = True
            return f"Marked '{task_to_complete}' as complete"
    return "Task not found"
    
    


view_all()