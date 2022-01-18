from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_wtf.file import FileField, FileAllowed
from wtforms.fields.core import SelectField

class StudentForm(FlaskForm):
    id = StringField ("id_number", [])
    oldid = StringField ("old_id", [])
    first = StringField ("first_name", [])
    last = StringField ("last_name", [])
    course = SelectField ("course", choices=[])
    year = SelectField('year_level', choices=[('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd'), ('4th', '4th'), ('5th', '5th')])
    gender = SelectField("gender", choices=[('Male','Male'),('Female','Female'),('Other','Other'),('Prefer not to say','Prefer not to say')])
    upload = FileField('image', validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Images only')])
    submit = SubmitField("Submit")

    def __init__(self, id = None,oldid = None, first = None, last = None, course = None, year = None, gender = None, upload = None):
        super().__init__()
        if id:
            self.process()
            self.id.default = id
            self.oldid.default = oldid
            self.first.default = first
            self.last.default = last
            self.course.default = course
            self.year.default = year
            self.gender.default = gender
            self.upload.default = upload
            self.process()


class CourseForm(FlaskForm):
    code = StringField("course_code", [])
    oldcode = StringField("old_course_code", [])
    name = StringField("course_name", [])
    college = SelectField("course_college", choices=[])
    submit = SubmitField("Submit")

    def __init__(self, code = None, oldcode = None ,name = None, college = None):
        super().__init__()
        if code:
            self.process()
            self.code.default = code
            self.oldcode.default = oldcode
            self.name.default = name
            self.college.default = college
            self.process()

class CollegeForm(FlaskForm):
    codec = StringField("college_code", [])
    oldcodec = StringField("old_college_code", [])
    namec = StringField("college_name", [])
    submit = SubmitField("Submit")

    def __init__(self, codec = None,oldcodec = None ,namec = None):
        super().__init__()
        if codec:
            self.process()
            self.codec.default = codec
            self.oldcodec.default = oldcodec
            self.namec.default = namec
            self.process()