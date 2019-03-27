import pymysql
class DatabaseOperations:
    def __init__(self,host_name,username,password,db_name, port):
        self.connection=pymysql.connect(host_name, username, password, db_name, port)

    def create_tables(self, query):
        try:
            cur= self.connection.cursor()
            cur.execute(query)
        except Exception as e:
            print(e)


database_operations=DatabaseOperations('localhost','root', 'Vaniadi_9', 'student', 1234)
join_two_tables='''select student1.studentname, marks.studentid from student
            #INNER JOIN
            #marks ON student1.studentid = marks.studentid'''
DatabaseOperations.create_tables(join_two_tables)