from flask import render_template, redirect, request, jsonify

from app.functions import forms
from . import students_bp, course_bp, college_bp
import app.models as models
from app.functions.forms import StudentForm, CourseForm, CollegeForm, SearchForm
from app import mysql
import cloudinary
import cloudinary.api
import cloudinary.uploader

def fetch_from_table(table_name, column):
    cursor = mysql.connection.cursor()
    sql = f"SELECT {column} from {table_name}"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

@students_bp.route('/main', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@students_bp.route('/viewstudents', methods=['POST', 'GET'])
def strindex():
    if request.method == 'GET':
        students = models.Students.allstudent()
        print(students, "allstudent")
        form = SearchForm(request.form)
        return render_template('ViewStudent.html', data=students, form=form, geturl='.strindex')
    if request.method == 'POST':
        form = SearchForm(request.form["searchbar"])
        print((form, "Searchbar"))
        students = models.Students.allstudent()
        final = []
        for data in students:
            for row in data:
                if form.searchbar.data.lower() in row.lower():
                    final.append(data)
                    break
        return render_template('ViewStudent.html', data=final, form=form)

@students_bp.route('/viewstudents/addstudent', methods=['POST', 'GET'])
def addstudent():
    form = StudentForm()
    for row in fetch_from_table('course', 'course_name'):
        course = str(row[0])
        form.course.choices += [(course, course)]
    if request.method == 'POST' and form.validate():
        print("in")
        if bool(form.upload.data):
            #print(form.upload.data)
            req = cloudinary.uploader.upload(form.upload.data.stream, public_id = form.id.data)
            req = req["secure_url"]
            print(req)
        else:
            req = None

        student = models.Students(id=form.id.data, first=form.first.data, last=form.last.data, course=form.course.data,
                           year=form.year.data, gender=form.gender.data, upload=req)
        print(student, "Studentsad")
        student.addstudent()
        return redirect('/viewstudents')
    else:
        return render_template('addStudent.html', form=form, geturl=".addstudent")

@students_bp.route("/viewstudents/editstudent", methods=['POST', 'GET'])
def editstudent():
    global oldid
    if request.method == 'GET':
        id = request.args.get("id")
        students = models.Students(id=id)
        studentinfo = students.searchstudent(id)
        form = StudentForm(studentinfo[0][0],studentinfo[0][0], studentinfo[0][1], studentinfo[0][2], studentinfo[0][3], studentinfo[0][4],)
        oldid = studentinfo[0][0]

        print(oldid, "oldid")
        print(form, "Form")
        print(students, "Student Info")
        print(studentinfo, "Info")
        for row in fetch_from_table('course', 'course_name'):
            course = str(row[0])
            form.course.choices += [(course, course)]
    else:
        form = StudentForm()
        for row in fetch_from_table('course', 'course_name'):
            course = str(row[0])
            form.course.choices += [(course, course)]
    cid = oldid

    if request.method == 'POST' and form.validate():

        if bool(form.upload.data):
            #print(form.upload.data)
            req = cloudinary.uploader.upload(form.upload.data.stream, public_id=form.id.data)
            req = req["secure_url"]
            #print(req)
        else:
            req = None

        student = models.Students(id=form.id.data, first=form.first.data, last=form.last.data, course=form.course.data,
                           year=form.year.data, gender=form.gender.data, upload=req, oldid=cid)
        print(student, "Edit Student")
        student.editstudent()
        return redirect('/viewstudents')
    else:
        return render_template('editStudent.html', form=form,geturl='.editstudent')

@students_bp.route("/viewstudents/deletestudent", methods=["POST"])
def deletestudent():
    id = request.form['id']
    if models.Students.deletestudent(id):
        return jsonify(success=True, message="Successfully deleted")
    else:
        return jsonify(success=False, message="Failed")

@course_bp.route('/viewcourses', methods=['POST', 'GET'])
def strindexcourse():
    if request.method == 'GET':
        course = models.Courses.allcourse()
        print(course)
        form = SearchForm(request.form)
        return render_template('ViewCourses.html', data=course, form=form)
    if request.method == 'POST':
        form = SearchForm(request.form["searchbar"])
        print((form, "Searchbar"))
        course = models.Courses.allcourse()
        final = []
        for data in course:
            for row in data:
                if form.searchbar.data.lower() in row.lower():
                    final.append(data)
                    break
        return render_template('ViewCourses.html', data=final, form=form)

@course_bp.route('/viewcourses/addcourse', methods=['POST', 'GET'])
def addcourse():
    form = CourseForm()
    for row in fetch_from_table('college', 'college_code'):
        college = str(row[0])
        form.college.choices += [(college, college)]
    if request.method == 'POST' and form.validate():
        print("in")
        course = models.Courses(code=form.code.data, name=form.name.data, college=form.college.data)
        print(course)
        course.addcourse()
        return redirect('/viewcourses')
    else:
        return render_template('addCourse.html', form=form, geturl=".addcourse")

@course_bp.route("/viewcourses/editcourse", methods=['POST', 'GET'])
def editcourse():
    global oldcode
    if request.method == 'GET':
        code = request.args.get("id")
        course = models.Courses(code=id)
        courseinfo = course.searchcourse(code)
        form = CourseForm(courseinfo[0][0], courseinfo[0][0], courseinfo[0][1],)
        oldcode = courseinfo[0][0]
        for row in fetch_from_table('college', 'college_code'):
            college = str(row[0])
            form.college.choices += [(college, college)]
    else:
        form = CourseForm()
        for row in fetch_from_table('college', 'college_code'):
            college = str(row[0])
            form.college.choices += [(college, college)]

    cord = oldcode

    if request.method == 'POST' and form.validate():
        course = models.Courses(code=form.code.data, name=form.name.data, college=form.college.data, oldcode=cord)
        course.editcourse()
        return redirect('/viewcourses')
    else:
        return render_template('editCourse.html', form=form, geturl='.editcourse')

@course_bp.route("/viewscoursess/deletecourse", methods=["POST"])
def deletecourse():
    id = request.form['id']
    print(id, "Delete ID")
    if models.Courses.deletecourse(id):
        return jsonify(success=True, message="Successfully deleted")
    else:
        return jsonify(success=False, message="Failed")

@college_bp.route('/viewcolleges', methods=['POST', 'GET'])
def strindexcollege():
    if request.method == 'GET':
        college = models.College.allcollege()
        print(college)
        form = SearchForm(request.form)
        print(form, "SearchForm")
        return render_template('ViewCollege.html', data=college, form=form)
    if request.method == 'POST':
        form = SearchForm(request.form["searchbar"])
        print((form, "Searchbar"))
        college = models.College.allcollege()
        print(college, "College Search")
        final = []
        print(final, "Final")
        for data in college:
            for row in data:
                if form.searchbar.data.lower() in row.lower():
                    final.append(data)
                    break
        return render_template('ViewCollege.html', data=final, form=form)

@college_bp.route('/viewcolleges/addcollege', methods=['POST', 'GET'])
def addcourse():
    form = CollegeForm()

    if request.method == 'POST' and form.validate():
        print("in")
        college = models.College(codec=form.codec.data, namec=form.namec.data)
        print(college)
        college.addcollege()
        return redirect('/viewcolleges')
    else:
        return render_template('addCollege.html', form=form, geturl=".addcollege")

@college_bp.route("/viewcolleges/editcollege", methods=['POST', 'GET'])
def editcollege():
    global oldcodec
    if request.method == 'GET':
        codec = request.args.get("id")
        college = models.College(codec=id)
        collegeinfo = college.searchcollege(codec)
        form = CollegeForm(collegeinfo[0][0],collegeinfo[0][1])
        oldcodec = collegeinfo[0][0]
        print(collegeinfo[0][1], "collegeeditform")
        print(collegeinfo, "collegeinfo")
    else:
        form = CollegeForm()

    cold = oldcodec

    if request.method == 'POST' and form.validate():
        college = models.College(codec=form.codec.data, namec=form.namec.data, oldcodec=cold)
        print(college, "College Edit")
        college.editcollege()
        return redirect('/viewcolleges')
    else:
        return render_template('editCollege.html', form=form, geturl='.editcollege')

@college_bp.route("/viewcolleges/deletecollege", methods=["POST"])
def deletecollege():
    id = request.form['id']
    if models.College.deletecollege(id):
        return jsonify(success=True, message="Successfully deleted")
    else:
        return jsonify(success=False, message="Failed")