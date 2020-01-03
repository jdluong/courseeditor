from flask import Flask, render_template, request, redirect, url_for
from .models import get_courses, create_course, delete_single_course, delete_all_courses
from .forms import CourseForm
from random import randint

from application import app

@app.route('/', methods = ['GET','POST'])
def index():
    if request.method == 'GET':

        return render_template('index.html')
    
    if request.method == 'POST':

        return redirect(url_for('home'))

@app.route('/home', methods = ['GET','POST'])
def home():
    form = CourseForm(request.form)
    if request.method == 'GET':
        pass
    
    if request.method  == 'POST':
        if 'delete' in request.form:
            print(request.form)
            delete_single_course(request.form['delete'])

        elif form.validate():
            print(request.form)
            course_data = (form.name.data,
                            form.professor.data,
                            form.letter_grade.data + form.sign_grade.data,
                            form.quarter.data + form.year.data,
                            form.thoughts.data)
            create_course(*course_data)
    
    courses = get_courses()
    return render_template('home.html',courses=courses,form=form)

@app.route('/surprise',methods = ['GET','POST'])
def surprise():

    if request.method == 'GET':
        pass

    if request.method == 'POST':
        pass

    return render_template('surprise.html')









# @app.route('/', methods = ['GET', 'POST'])
def index_old():
    
    # true when this route is visited for any reason
    if request.method == 'GET':
        pass

    # true when a submit button is pressed
    if request.method == 'POST':
        # this is actually posting a new course
        if request.form.get('course'):
            # use request.form.get(the value of 'name' attribute in input tag)
            course = request.form.get('course')
            random = request.form.get('random')
            create_post(course)
            # this is redirecting to another page after submitting a course; fun!
            # if 2 == 2:
            #     return redirect('/surprise')
        # this is deleting a single course
        elif request.form.get('delete_single'):
            course_to_delete = request.form.get('delete_single')
            delete_single_course(course_to_delete)
        # THIS IS DELETING ALL COURSES
        else:
            delete_all_courses()
    
    # this is to get all the courses from database, passing into html file,
    # so html file, with python, can use that variable to iteratively format
    # each course in html
    courses = get_courses()
    if request.method == 'POST' and request.form.get('course'):
        return render_template('index.html', courses=courses, random=random)
    else:
        return render_template('index.html', courses=courses)

# @app.route('/surprise',methods = ['GET','POST'])
def surprise_old():

    if request.method == 'GET':
        pass

    if request.method == 'POST':
        pass

    return render_template('surprise.html')
