import streamlit as st
import mysql.connector

from main import *
# from create import create
# # from database import create_table
# from delete import delete
# from read import read
# from update import update

def main():
    st.title("Leetcode-Like coding contest")
    st.header("Using User Table")
    menu = ["Add User", "View User", "Edit User", "Remove User","Query"]
    choice = st.sidebar.selectbox("Menu", menu)


    if choice == "Add User":
        st.subheader("Enter User Details:")
        create()

    elif choice == "View User":
        st.subheader("View User Details:")
        read()

    elif choice == "Edit User":
        st.subheader("Edited User Details:")
        update()

    elif choice == "Remove User":
        st.subheader("Delete User:")
        delete()

    elif choice == "Query":
        st.subheader("Enter Query:")
        query()

    else:
        st.subheader("About User")


if __name__ == '__main__':
    main()