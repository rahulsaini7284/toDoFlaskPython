from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_db(app):
    db.init_app(app)
    return db


class Person(db.Model):
    __tablename__ = "Persons"
    pid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=None)
    age = db.Column(db.Integer, nullable=None)
    city = db.Column(db.Text, nullable=None)
    isAdult = db.Column(db.Boolean)

    def __repr__(self):
        print(f"Person with name {self.name} and age {self.age}")
