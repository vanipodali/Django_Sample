import pymysql
import random
class DatabaseOperations:
    def __init__(self, host_name, username, password, db_name, port):
        self.connection = pymysql.connect(host_name, username, password, db_name, port)

    def create_tables(self,create_table_query):
        try:
            cur=self.connection.cursor()
            cur.execute(create_table_query)
        except Exception as e:
            print(e)

    def insert_student_values(self,insert_query):
        try:
            for i in range(1,100):
                student_id=random.randint(1,100)
                student_name='student-'+str(student_id)
                cur=self.connection.cursor()
                cur.execute(insert_query,(student_id,student_name))
            self.connection.commit()
        except Exception as e:
            print(e)

    def insert_subjects(self,insert_query):
        try:
            for i in range(1,6):
                subject_id=random.randint(1,6)
                subject_name='subject-'+str(subject_id)
                cur=self.connection.cursor()
                cur.execute(insert_query,(subject_id,subject_name))
            self.connection.commit()
        except Exception as e:
            print(e)
    def insert_marks(self,insert_query):
        try:

            for i in range(1,1000):
                marks_id=random.randint(1,1000)
                student_id=random.randint(1,100)
                subject_id=random.randint(1,6)
                marks=random.randint(1,100)
                cur=self.connection.cursor()
                cur.execute(insert_query,(marks_id,student_id,subject_id,marks))
            self.connection.commit()
        except Exception as e:
            print(e)
    def update_values(self,table_name,col_names,values):
        pass

    def get_values(self,query):
        try:
            cur=self.connection.cursor()
            cur.execute(query)
        except Exception as e:
            print(e)

DatabaseOperations=DatabaseOperations('localhost','root', 'Vaniadi_9', 'student', 1234)
create_subject_query = '''CREATE TABLE `subjects` (
              `subject_id` int,
              `subject_name` varchar(100) DEFAULT NULL
            ) '''
DatabaseOperations.create_tables(create_subject_query)

#insert values into the student

insert_student_records_query='''
insert student ( student_id,student_name) value(%s,%s)
'''


# database_operations.insert_values(insert_student_records_query)

# insert values into subject

insert_subjects_query='''
insert subjects ( subject_id,subject_name) value(%s,%s)
'''


# database_operations.insert_subjects(insert_subjects_query)


#insert_marks

insert_marks_query='''
insert marks ( marks_id,student_id, subject_id,marks) value(%s,%s,%s,%s)
'''


DatabaseOperations.insert_marks(insert_marks_query)