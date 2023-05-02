from flask import Flask, render_template, request, render_template_string, url_for, redirect, flash
from markupsafe import Markup, escape
from flask_sqlalchemy import SQLAlchemy
from database import db
from models.students import Student
from forms.editstudent import EditStudentForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'abcdsecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myapp.db'
db.init_app(app) # Initialize SQLAlchemy with app
with app.app_context():
    db.create_all()


#Routes are defined below
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/maindatabase')#A main page that shows the user's names and emails in a list and has buttons that delete users from the database.
def maindatabase():
    all_students = Student.query.all()
    return render_template('maindatabase.html', students=all_students)

@app.route('/create', methods=['GET', 'POST'])#A create page in which you can create new users in the database.
def create():
    if request.method == 'POST':
        student = Student(first_name=request.form['first_name'], email=request.form['email'])
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('maindatabase'))
    return render_template('create.html')

@app.route('/update')#An update page in which you can edit users in the database.
def update():
    all_students = Student.query.all()
    return render_template('update.html', students=all_students)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_student(id):
    goodbye_student = Student.query.get(id)
    db.session.delete(goodbye_student)
    db.session.commit() #commits changes
    return redirect(url_for('maindatabase')) #once deleted, returns to the main database page

@app.route('/edit/<int:id>', methods=['GET','POST'])
def edit_student(id):
    edit_student = Student.query.get(id)
    form = EditStudentForm(obj=edit_student)
    if form.validate_on_submit():
        form.populate_obj(edit_student)
        db.session.commit()
        flash('you changed it, nice')
        return redirect(url_for('update')) #once deleted, returns to the update page
    return render_template('editstudent.html', form=form, student=edit_student)

@app.route('/viewstyles') #a practice page
def view_styles():
    return render_template('viewstyles.html')

#Some macros below
@app.template_global() #make an html link using python function in an .html file
def link_with_class(text, url, css_class):
    link = f'<a href="{url}" class="{css_class}">{text}</a>'
    return Markup(link) #used Markup to render html correctly

@app.template_global() #make a delete button using python function in an .html file
def delete_student_button(student):
    button = f'''<form method="POST" action="{url_for('delete_student', id=escape(student.id))}">
            <button type="submit">Delete</button>
        </form>'''
    return Markup(button)

#Style
@app.route('/static/styles.css')
def serve_css():
    return app.send_static_file('styles.css') #a simple style sheet

if __name__ == '__main__':
    app.run(debug=True)