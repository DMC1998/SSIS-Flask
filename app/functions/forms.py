from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_wtf.file import FileField, FileAllowed
from wtforms.fields.core import SelectField

class StudentForm(FlaskForm):
    id = StringField ("id_number", [])
    first = StringField ("first_name", [])
    last = StringField ("last_name", [])
    course = SelectField ("course", choices=[])
    year = SelectField('year_level', choices=[('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd'), ('4th', '4th'), ('5th', '5th')])
    gender = SelectField("gender", choices=[('Male','Male'),('Female','Female'),('Other','Other'),('Prefer not to say','Prefer not to say')])
    upload = FileField('image', validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Images only')])
    oldid = StringField ("old_id", [])
    submit = SubmitField("Submit")

    def __init__(self, id = None, first = None, last = None, course = None, year = None, gender = None, upload = None,oldid = None):
        super().__init__()
        if id:
            self.process()
            self.id.default = id
            self.first.default = first
            self.last.default = last
            self.course.default = course
            self.year.default = year
            self.gender.default = gender
            self.upload.default = upload
            self.oldid.default = oldid
            self.process()


class CourseForm(FlaskForm):
    code = StringField("course_code", [])
    name = StringField("course_name", [])
    college = SelectField("course_college", choices=[])
    oldcode = StringField("old_course_code", [])
    submit = SubmitField("Submit")

    def __init__(self, code = None,name = None, college = None, oldcode = None ):
        super().__init__()
        if code:
            self.process()
            self.code.default = code
            self.name.default = name
            self.college.default = college
            self.oldcode.default = oldcode
            self.process()

class CollegeForm(FlaskForm):
    codec = StringField("college_code", [])
    namec = StringField("college_name", [])
    oldcodec = StringField("old_college_code", [])
    submit = SubmitField("Submit")

    def __init__(self, codec = None,namec = None,oldcodec = None):
        super().__init__()
        if codec:
            self.process()
            self.codec.default = codec
            self.namec.default = namec
            self.oldcodec.default = oldcodec
            self.process()

class SearchForm(FlaskForm):
    searchbar = StringField("search", [])
    submit = SubmitField("Submit")

    def __init__(self, searchbar = None):
        super().__init__()
        if searchbar:
            self.process()
            self.searchbar.default = searchbar
            self.process()