import pandas as pd
import streamlit as st
from database import *
from datetime import date

def create():
    col1, col2 = st.columns(2)
    with col1:
        fname = st.text_input("First Name:")
        lname = st.text_input("Last Name:")
        uni = st.text_input("University:")
    with col2:
        email_id = st.text_input("Email ID:")
        dob = st.date_input("DateOFBirth",date(2002,1,1),date(1982,1,1),date(2021,1,1))
        gender = st.radio("Gender",["Male", "Female"])
        print(dob)
    if st.button("Add User"):
        try:
            add_data(fname, lname, uni, email_id, dob, gender)
            st.success("Successfully added User: {}".format(fname))
        except Exception as e:
            st.info("You might have enter details in wrong format: Check Mail_ID again")
            st.info("Mail should be of format ___@____.com")


def read():
    result = view_all_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Fname','Lname','University' ,'DOB' ,'Gender','email_id'])
    with st.expander("View all User"):
        st.dataframe(df)


def update():
    result = view_all_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Fname','Lname','University' ,'DOB' ,'Gender','email_id'])
    with st.expander("Current Users"):
        st.dataframe(df)
    list_of_users = [str(i[0]+" "+i[1]) for i in view_only_user_names()]
    selected_name = st.selectbox("Users to Edit", list_of_users)
    selected_result = get_details(selected_name)
    # st.write(selected_result)
    if selected_result:
        fname = selected_result[0][0]
        lname = selected_result[0][1]
        university = selected_result[0][2]
        dob = selected_result[0][3]
        Gender = selected_result[0][4]
        email_id = selected_result[0][5]

        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_fname = st.text_input("First name:", fname)
            new_lname = st.text_input("Last Name:", lname)
            new_university = st.text_input("University", university)
        with col2:
            new_email_id = st.text_input("Email ID:",email_id)
            new_dob = st.date_input("DateOFBirth",dob,date(1982,1,1),date(2021,1,1))
            new_gender = st.radio("Gender",["Male", "Female"])


        if st.button("Update User"):
            edit_details(new_fname, new_lname,new_university, new_email_id, new_dob, new_gender, fname, lname, university,email_id, dob , Gender)
            st.success("Successfully updated")

    result2 = view_all_data()
    df = pd.DataFrame(result2, columns=['Fname','Lname','University' ,'DOB' ,'Gender','email_id'])
    with st.expander("Updated Users"):
        st.dataframe(df)

def delete():
    result = view_all_data()
    df = pd.DataFrame(result, columns=['Fname','Lname','University' ,'DOB' ,'Gender','email_id'])
    with st.expander("Current Users"):
        st.dataframe(df)

    list_of_users = [str(i[0]+" "+i[1]) for i in view_only_user_names()]
    selected_user = st.selectbox("User to Delete", list_of_users)
    st.info("Do you want to delete ::{}".format(selected_user))
    if st.button("Delete User"):
        delete_data(selected_user)
        st.success("User has been deleted successfully")
    new_result = view_all_data()
    df1 = pd.DataFrame(new_result, columns=['Fname','Lname','University' ,'DOB' ,'Gender','email_id'])
    with st.expander("Updated Users"):
        st.dataframe(df1)


def query():
    que = st.text_area("Enter your query here: ")
    if st.button("Submit Query"):
        try:
            res = run_query(que)
            x=pd.DataFrame(res)
            st.table(x)
            st.success("Query accepted")
        except Exception as e:
            st.info("ENTERED QUERY IS WRONG")

        
     