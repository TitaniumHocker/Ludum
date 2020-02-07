# -*- coding: utf-8 -*-
from flask import Flask
from .extensions import db
# Migrations imports
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from flask_security import (
        SQLAlchemyUserDatastore,
        Security, current_user
        )

app = Flask(__name__)
app.config.from_pyfile('config.py')
db.init_app(app)

# Migrations setup
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


# Admin panel setup
from .models import *
from .admin_security import (TaskAdminView,
        CategoryAdminView, HomeAdminView)

admin = Admin(app, 'Ludum', index_view=HomeAdminView(name='Home'))
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Role, db.session))
admin.add_view(TaskAdminView(Task, db.session))
admin.add_view(CategoryAdminView(Category, db.session))

# Security

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
