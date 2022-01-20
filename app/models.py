from app import mysql

#from werkzeug.security import generate_password_hash, check_password_hash

def getlatest():
    cursor = mysql.connection.cursor()
    sql = f"SELECT id_number FTOM students ORDER BY id_number DESC LIMIT 1"
    cursor.execute(sql)
    ids = cursor.fetchall()

    return ids


class Students(object):

    def __init__(self, id = None, first = None, last = None, course = None,
                 year = None, gender = None, upload = None, oldid = None):
        self.id = id
        self.first = first
        self.last = last
        self.course = course
        self.year = year
        self.gender = gender
        self.upload = upload
        self.oldid = oldid

    def addstudent(self):
        cursor = mysql.connection.cursor()
        sql = f"INSERT INTO students(id_number,first_name,last_name,course,year_level,gender,image) \
                VALUES('{self.id}','{self.first}','{self.last}','{self.course}','{self.year}','{self.gender}', '{self.upload}')"
        print(sql)
        cursor.execute(sql)
        mysql.connection.commit()

    def editstudent(self):
        cursor = mysql.connection.cursor()
        print(self.id)
        if self.upload:
            sql = f"UPDATE students SET id_number ='{self.id}',first_name ='{self.first}',last_name ='{self.last}'," \
                  f"course ='{self.course}',year_level ='{self.year}'," \
                  f"gender ='{self.gender}', image ='{self.upload}' WHERE id_number = '{self.oldid}'"
            print(sql, "With Image")
        else:
            sql = f"UPDATE students SET id_number ='{self.id}',first_name ='{self.first}',last_name ='{self.last}'," \
                  f"course ='{self.course}',year_level ='{self.year}'," \
                  f"gender ='{self.gender}' WHERE id_number = '{self.oldid}'"
            print(sql, "Without Image")
        try:
            cursor.execute(sql)
        except Exception as e:
            print(e)
        mysql.connection.commit()


    @classmethod
    def allstudent(cls):
        cursor = mysql.connection.cursor()
        sql = "SELECT * from students"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    @classmethod
    def datastudent(cls):
        cursor = mysql.connection.cursor()
        sql = "SELECT * from students"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    @classmethod
    def deletestudent(cls, id):
        try:
            cursor = mysql.connection.cursor()
            sql = f"DELETE from students where id_number = '{id}'"
            cursor.execute(sql)
            mysql.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def searchstudent(cls, id):
        cursor = mysql.connection.cursor()
        sql = f"SELECT * from students where id_number='{id}'"
        cursor.execute(sql)
        ids = cursor.fetchall()
        return ids

class Courses(object):

    def __init__(self, code = None, name = None, college = None, oldcode = None):
        self.code = code
        self.name = name
        self.college = college
        self.oldcode = oldcode

    def addcourse(self):
        cursor = mysql.connection.cursor()
        sql = f"INSERT INTO course(course_code,course_name,course_college) \
                VALUES('{self.code}','{self.name}','{self.college}')"
        print(sql)
        cursor.execute(sql)
        mysql.connection.commit()

    def editcourse(self):
        cursor = mysql.connection.cursor()
        print(self.code)
        sql = f"UPDATE course SET course_code ='{self.code}',course_name ='{self.name}',course_college ='{self.college}'" \
              f"WHERE course_code = '{str(self.oldcode)}'"
        try:
            cursor.execute(sql)
        except Exception as e:
            print(e)
        mysql.connection.commit()


    @classmethod
    def allcourse(cls):
        cursor = mysql.connection.cursor()

        sql = "SELECT * from course"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    @classmethod
    def datacourse(cls):
        cursor = mysql.connection.cursor()
        sql = "SELECT * from course"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    @classmethod
    def deletecourse(cls, code):
        try:
            cursor = mysql.connection.cursor()
            sql = f"DELETE from course where course_code = '{code}'"
            cursor.execute(sql)
            mysql.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def searchcourse(cls, code):
        cursor = mysql.connection.cursor()
        sql = f"SELECT * from course where course_code='{code}'"
        cursor.execute(sql)
        codes = cursor.fetchall()
        return codes

class College(object):

    def __init__(self, codec = None, namec = None, oldcodec = None):
        self.codec = codec
        self.namec = namec
        self.oldcodec = oldcodec

    def addcollege(self):
        cursor = mysql.connection.cursor()
        sql = f"INSERT INTO college(college_code,college_name) \
                VALUES('{self.codec}','{self.namec}')"
        print(sql)
        cursor.execute(sql)
        mysql.connection.commit()

    def editcollege(self):
        cursor = mysql.connection.cursor()
        print(self.codec)
        sql = f"UPDATE college SET college_code ='{self.codec}',college_name ='{self.namec}' WHERE college_code = '{str(self.oldcodec)}'"
        try:
            cursor.execute(sql)
        except Exception as e:
            print(e)
        mysql.connection.commit()


    @classmethod
    def allcollege(cls):
        cursor = mysql.connection.cursor()

        sql = "SELECT * from college"
        print(sql, "ALL COLLEGE SQL")
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    @classmethod
    def datacollege(cls):
        cursor = mysql.connection.cursor()
        sql = "SELECT * from college"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    @classmethod
    def deletecollege(cls, codec):
        try:
            print(codec, "codec delete")
            cursor = mysql.connection.cursor()
            sql = f"DELETE from college where college_code = '{codec}'"
            cursor.execute(sql)
            mysql.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def search(cls, codecs):
        cursor = mysql.connection.cursor()
        sql = f"SELECT * from college where college_code='{codecs}'"
        print(sql, "SEARCH COLLEGE")
        cursor.execute(sql)
        codecs = cursor.fetchall()
        return codecs
