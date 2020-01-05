from wtforms import Form, StringField, SelectField, TextAreaField, SubmitField, validators
from datetime import datetime

class Msgs:
    general = "Please enter a value"

class CourseForm(Form):
    todays_yr = datetime.today().year
    name = StringField('Name', [validators.InputRequired(Msgs.general), validators.Length(max=20)])
    instructor = StringField('Instructor', [validators.InputRequired(Msgs.general), validators.Length(max=255)])
    letter_grade = SelectField('Grade', 
                                choices=[('A','A'),('B','B'),('C','C'),('D','D'),('F','F')])
    sign_grade = SelectField('+/-',
                                choices=[('+','+'),('-','-'),(' ',' ')])
    quarter = SelectField('Quarter',
                                choices=[('F','Fall'),('W','Winter'),('SP','Spring'),('SM','Summer')])
    year = SelectField('Year', 
                                choices=[(str(yr)[-2::],str(yr)[-2::]) for yr in range(todays_yr-10,todays_yr+10)],
                                default=(str(todays_yr)[-2::])) # is this inefficient
    thoughts = TextAreaField('Thoughts', [validators.Length(min=0,max=255)])

    submit = SubmitField('Submit')
    cancel = SubmitField('Cancel')
    
