from wtforms import Form, StringField, SelectField, TextAreaField, validators
from datetime import datetime

class Msgs:
    general = "Please enter a value"

class CourseForm(Form):
    todays_yr = datetime.today().year
    quarter = SelectField('Quarter',
                                choices=[('F','Fall'),('W','Winter'),('S','Spring'),('SUM','Summer')])
    year = SelectField('Year', 
                                choices=[(str(yr)[-2::],str(yr)[-2::]) for yr in range(todays_yr-10,todays_yr+10)],
                                default=(str(todays_yr)[-2::])) # is this inefficient
    name = StringField('Name', [validators.InputRequired(Msgs.general)])
    professor = StringField('Prof', [validators.InputRequired(Msgs.general)])
    letter_grade = SelectField('Grade', 
                                choices=[('A','A'),('B','B'),('C','C'),('D','D'),('F','F')])
    sign_grade = SelectField('+/-',
                                choices=[('+','+'),('-','-'),('','')])
    thoughts = TextAreaField('Thoughts', [validators.Length(min=0,max=255)])
