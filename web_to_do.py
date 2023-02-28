import streamlit as st
import functions as f


todos = f.get_todos()
def add_todo():
    todo = st.session_state['new_todo']
    todos.append(todo+'\n')
    f.add_todos(todos)

st.subheader("Please enter to do")
st.write("this app to increase dddd")
st.title("My ToDo App")

for index,todo in enumerate(todos):
    is_checked = st.checkbox(todo,key=todo)
    if is_checked:
        todos.pop(index)
        f.add_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()



st.text_input(label='',placeholder='enter your todo please',
              on_change=add_todo,key='new_todo')






