import streamlit as st
import functions

todos = functions.get_todos()
st.title("My Todo App")
st.subheader("todo App")
st.write("this app is todo app")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter here..", placeholder="add new todo")
