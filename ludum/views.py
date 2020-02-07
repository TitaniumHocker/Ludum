# -*- coding: utf-8 -*-
from flask import (
        render_template,
        url_for, abort,
        redirect, request)
from .app import app
from .extensions import db
from .models import *


def generate_alert(alert_type, message):
    return f'''
    <div class="alert alert-{alert_type} alert-dismissible fade show" role="alert">
	{message}
    <button type="button" class="close" data-dismiss="alert" aria-label="Close">
		<span aria-hidden="true">&times;</span>
	</button>
    </div>
    '''

@app.route('/')
def index_page():
    return render_template('index.html', page_title='Mainpage')

@app.route('/tasks')
def tasks_page():
    print(request.path)
    tasks = [task.properties for task in Task.query.all()]
    categories = [category for category in Category.query.all()]
    tasks_by_categories = {}
    for category in categories:
        el = { category.title: [task for task in tasks if category in task['categories']] }
        tasks_by_categories.update(el)
    return render_template('tasks.html', page_title='Tasks',
            categories=categories, tasks_by_categories=tasks_by_categories)

@app.route('/about')
def about_page():
    return render_template('about.html', page_title='About')

@app.route('/tasks/<slug>', methods=['GET', 'POST'])
def task_page(slug):
    task = Task.query.filter(Task.slug==slug).first_or_404()
    if request.method == 'GET':
        return render_template('task.html', page_title=task.title, task=task.properties)
    answ = request.form.get('answ', '')
    if answ == task.answer:
        return render_template('task.html',
                page_title=task.title,
                task=task.properties,
                alert=generate_alert('success', f'Ответ верный, часть ключа: {task.reward}'))
    return render_template('task.html',
            page_title=task.title,
            task=task.properties,
            alert=generate_alert('danger', 'Ответ неверный, ищи лучше.'))



