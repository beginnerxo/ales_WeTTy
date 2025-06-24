import streamlit as st
import local_logic


st.title('WeTTy To Do :blue[List] :kiss:')



col1, col2  = st.columns([3,1])



with col1:
    new_task = st.text_input("Add a task", key = "user_input")
    
with col2:
    if st.button("➕ Add"):
        if new_task.strip():
            st.success(local_logic.add(new_task.strip()))
        else:
            st.warning("Task cannot be empty.")


#View task

st.subheader("📋 Current Tasks")
all_tasks = local_logic.view_all()
if all_tasks:
    for task in all_tasks:
        st.write(task)
 
 


              
#view = local_logic.view_all()
#st.success(vie
