# -*- coding: utf-8 -*-
from flask import redirect, url_for, request
from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView
from flask_security import current_user


class AdminMixin:
    def is_accessible(self):
        return current_user.has_role('admin')
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('security.login', next=request.url))

class SluggedModelView(ModelView):
    def on_model_change(self, form, model, is_created):
        model.generate_slug()
        return super(SluggedModelView, self).on_model_change(form, model, is_created)

class AdminView(AdminMixin, ModelView): pass

class HomeAdminView(AdminMixin, AdminIndexView): pass

class TaskAdminView(AdminMixin, SluggedModelView):
    form_columns = ['title', 'body', 'answer', 'reward', 'categories']

class CategoryAdminView(AdminMixin, SluggedModelView):
    form_columns = ['title']



