# -*- coding: utf-8 -*-
from flask_security import UserMixin, RoleMixin
from datetime import datetime
from .extensions import db
import re


def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s)


roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
    )

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(256))
    active = db.Column(db.Boolean())
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(32), unique=True)
    description = db.Column(db.String(256))


task_category = db.Table('task_category',
            db.Column('task_id', db.Integer, db.ForeignKey('task.id')),
            db.Column('category_id', db.Integer, db.ForeignKey('category.id'))
        )

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    slug = db.Column(db.String(128), unique=True, nullable=False)
    body = db.Column(db.Text())
    answer = db.Column(db.String(128), nullable=False)
    reward = db.Column(db.String(128), nullable=False)
    created = db.Column(db.DateTime, default=datetime.now())
    categories = db.relationship('Category', secondary=task_category,
            backref=db.backref('tasks', lazy='dynamic'))

    def __init__(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Task, self).__init__(*args, **kwargs)

    def __repr__(self):
        return f'<Task id: {self.id}, title: {self.title}>'

    def generate_slug(self):
        self.slug = slugify(self.title)

    @property
    def properties(self):
        properties = {
                    'title': self.title,
                    'body': self.body,
                    'categories': self.categories,
                    'slug': self.slug
                }
        return properties


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    slug = db.Column(db.String(128), unique=True, nullable=False)

    def generate_slug(self):
        self.slug = slugify(self.title)

    def __init__(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).__init__(*args, **kwargs)

    def __repr__(self):
        return f'<Category id: {self.id}, title: {self.title}>'

