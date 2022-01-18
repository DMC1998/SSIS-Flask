from flask import Blueprint

students_bp = Blueprint('students',__name__)
course_bp  = Blueprint('course',__name__)
college_bp = Blueprint('college', __name__)

from . import controller
