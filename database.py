import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="code_contest_project_560"
)
c = mydb.cursor()


# def create_table():
#     c.execute('CREATE TABLE IF NOT EXISTS Train (Train_No int, Name varchar(30), Train_Type varchar(20), Source varchar(20), Destination varchar(20), Availability varchar(5));')


def add_data(fname,lname,uni,email_id,dob,gender):
    c.execute("select last_value(U_ID) from user")
    x=(c.fetchall()) 
    id = x[-1][0] + 1  
    c.execute('INSERT INTO user (U_ID,fname, lname, University, email_id, dob, gender) VALUES (%s,%s,%s,%s,%s,%s,%s);',
              (id,fname, lname, uni, email_id, dob, gender))
    mydb.commit()


def view_all_data():
    c.execute('SELECT Fname,Lname,University ,DOB ,Gender,email_id FROM User')
    data = c.fetchall()
    return data


def view_only_user_names():
    c.execute('SELECT fname,lname FROM user')
    data = c.fetchall()
    return data


def get_details(selected_name):
    x = selected_name.strip().split()
    c.execute(f'SELECT Fname,Lname,University ,DOB ,Gender,email_id FROM user WHERE fname="{x[0]}" and lname="{x[1]}"')
    data = c.fetchall()
    return data


def edit_details(new_fname, new_lname,new_university, new_email_id, new_dob, new_gender, fname, lname, university,email_id, dob , Gender):
    c.execute("UPDATE User SET fname=%s, lname=%s, University=%s, email_id=%s, dob=%s, gender=%s WHERE "
              "fname=%s and lname=%s and University=%s and email_id=%s and dob=%s and gender=%s ", 
              (new_fname, new_lname,new_university, new_email_id, new_dob, new_gender, fname, lname, university,email_id, dob , Gender))
    mydb.commit()
    #data = c.fetchall()
    #return data
    pass


def delete_data(selected_name):
    x = selected_name.strip().split()
    c.execute('DELETE FROM user WHERE fname="{}" and lname="{}"'.format(x[0],x[1]))
    mydb.commit()

def run_query(que):
    mydb2 = mysql.connector.connect(
    host="localhost",
    user="root",
    database="code_contest_project_560"
    )
    c2 = mydb2.cursor(dictionary=True)

    try:
        c2.execute(que)
        return c2.fetchall()
        
    except mysql.connector.Error as e:
        return e




print("done")