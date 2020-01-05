from flask import Flask, render_template, request, redirect, url_for
from .models import get_courses, get_single_course, create_course, delete_single_course, delete_all_courses
from .forms import CourseForm
from random import randint

from application import app

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'GET':

        return render_template('index.html')
    
    if request.method == 'POST':

        return redirect(url_for('home'))


@app.route('/home', methods=['GET','POST'])
def home():

    if request.method == 'GET':
        pass
    
    if request.method  == 'POST':
        if 'delete' in request.form:
            delete_single_course(request.form['delete'])
        elif 'edit' in request.form:
            return redirect(url_for('edit', id=request.form['edit']))
        elif 'route_add' in request.form:
            return redirect(url_for('add'))
    
    courses = get_courses()
    return render_template('home.html',courses=courses,home=True)


@app.route('/home/add', methods=['GET','POST'])
def add():
    form = CourseForm(request.form)
    form.submit.label.text = 'Add Course'

    if request.method == 'GET':
        pass

    if request.method == 'POST':
        print(request.form)
        if 'delete' in request.form:
            delete_single_course(request.form['delete'])
        elif 'edit' in request.form:
            return redirect(url_for('edit', id=request.form['edit']))

        elif 'submit' in request.form and form.validate():
            course_data = (form.name.data,
                            form.instructor.data,
                            form.letter_grade.data,
                            form.sign_grade.data,
                            form.quarter.data,
                            form.year.data,
                            form.thoughts.data)
            create_course(*course_data)
            return redirect(url_for('home'))
        elif 'cancel' in request.form:
            return redirect(url_for('home'))

    courses = get_courses()
    return render_template('add.html', courses=courses, home=False, form=form)


def set_data(form,course):
    # all fields except buttons (last two)
    for ind, field in enumerate(list(form._fields)[:-2],1):
        form[field].data = course[ind]

@app.route('/home/edit', methods=['GET','POST'])
def edit():
    form = CourseForm(request.form)
    form.submit.label.text = 'Confirm'
    
    if request.method == 'GET':
        pass

    if request.method == 'POST':
        if 'delete' in request.form:
            delete_single_course(request.form['delete'])
        elif 'edit' in request.form:
            return redirect(url_for('edit', id=request.form['edit']))

        elif 'submit' in request.form and form.validate():
            
            return redirect(url_for('home'))
        elif 'cancel' in request.form:
            return redirect(url_for('home'))
    
    course = get_single_course(request.args['id'])
    set_data(form,course)
    courses = get_courses()
    return render_template('edit.html', courses=courses, home=False, form=form)


@app.route('/surprise',methods = ['GET','POST'])
def surprise():

    if request.method == 'GET':
        pass

    if request.method == 'POST':
        pass

    return render_template('surprise.html')



