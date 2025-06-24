import streamlit as st
import local_logic


st.title('WeTTy To Do :blue[List] :kiss:')

#input form
with st.form("add_task_form", clear_on_submit=True):
    new_task = st.text_input("Add a task", key="new_task_input")
    submitted = st.form_submit_button("➕ Add")
    if submitted and new_task.strip():
        st.success(local_logic.add(new_task.strip()))
    



#View task

st.subheader("📋 Current Tasks")

all_tasks = local_logic.view_all()

if not all_tasks:
    st.info("No tasks added yet.")
    
    
else:
    for i, task in enumerate(all_tasks):
        task_text = task["text"]
        is_done = task["done"]

        # Use 3 columns: checkbox, task label, delete button
        col1, col2, col3 = st.columns([0.1, 5, 0.5])
        
        with col1:
            checked = st.checkbox("", value=is_done, key=f"check_{i}")
        
        with col2:
            if is_done:
                st.markdown(
                    f"<span style='color: grey; font-style: italic;'>{task_text}</span> "
                    f"<span style='background-color: #d3f9d8; color: green; padding: 2px 6px; border-radius: 6px;'>DONE</span>",
                    unsafe_allow_html=True
                )
            else:
                st.write(task_text)

        with col3:
            if st.button("❌", key=f"delete_{i}"):
                local_logic.delete(task_text)
                st.rerun()

        # Handle completion
        if checked and not is_done:
            local_logic.complete(task_text)
            st.rerun()
        # Display visual badge if task is done
 
 #delete Task 
 
 
 


              
#view = local_logic.view_all()
#st.success(vie
