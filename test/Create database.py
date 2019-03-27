import pymysql
con = pymysql.connect(user='root', passwd='Vaniadi_9', host='localhost', port=1234)
#mycursor = con.cursor()
#mycursor.execute("Create database student")
try:
    create_schema_Cursor = con.cursor()
    Create_Schema_Query = 'create schema student'
    create_schema_Cursor.execute(Create_Schema_Query)
except Exception as e:
    print(e)

#create database
try:
    create_database_query = 'create database student '
    create_database_cursor = con.cursor()
    create_database_cursor.execute(create_database_query)
except Exception as e:
    print(e)

# use database

try:
    create_database_query = 'USE student'
    create_database_cursor = con.cursor()
    create_database_cursor.execute(create_database_query)
except Exception as e:
    print(e)

#Create table student
try:
    create_student_query = 'CREATE TABLE student1(student_id mediumtext,student_name Varchar(100) Default NULL)'
    create_table_cursor = con.cursor()
    create_table_cursor.execute(create_student_query)
except Exception as e:
    print(e)

#Create table subject
try:
    create_subject_query = 'CREATE TABLE subject(subject_id mediumtext,subject_name Varchar(100) Default NULL)'
    create_table_cursor = con.cursor()
    create_table_cursor.execute(create_subject_query)
except Exception as e:
    print(e)

# Create table marks
try:
    create_marks_query = 'CREATE TABLE marks(marks_id int ,student_id int, subject_id int, marks float Default NULL)'
    create_table_cursor = con.cursor()
    create_table_cursor.execute(create_marks_query)
except Exception as e:
    print(e)

