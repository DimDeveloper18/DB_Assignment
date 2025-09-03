from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

dbase = SQLAlchemy()

class Customer(UserMixin, dbase.Model):
    id = dbase.mapped_column(dbase.Integer, primary_key=True)
    username = dbase.mapped_column(dbase.String(50), unique=True)
    password = dbase.mapped_column(dbase.String(50))

    def __str__(self):
        return self.username