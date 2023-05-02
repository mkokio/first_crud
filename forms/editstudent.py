from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class EditStudentForm(FlaskForm): #StudentForm as a subclass of FlaskForm
    first_name = StringField("Student's first name")
    email = StringField('Email')
    submit = SubmitField('Confirm Changes, yo')

'''
Basically this is what it would look like in HTML
<form method="POST">
<label for="first_name">Student's first name:</label> <input type="text" id="first_name" name="first_name">
<label for="email">Email:</label> <input type="email" id="email" name="email">
<button type="submit">Confirm Changes, yo</button>
</form>
'''