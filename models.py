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
    
class CustomerComment(dbase.Model):
    id = dbase.mapped_column(dbase.Integer, primary_key=True)
    msgname = dbase.mapped_column(dbase.String(80), nullable=False)
    comment = dbase.mapped_column(dbase.Text, nullable=False)
    writer_id = dbase.mapped_column(dbase.Integer, dbase.ForeignKey('customer.id'), nullable=False)

    writer = dbase.relationship('Customer', backref=dbase.backref('customer_comments', lazy=True))

    def __str__(self):
        return f'"{self.msgname}" by {self.writer.username}'