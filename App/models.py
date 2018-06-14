from App.ext import db


class Student(db.Model):

    __tablename__ = 'student'

    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    name = db.Column(db.VARCHAR(16))
    age = db.Column(db.INTEGER)
    s_grade_id = db.Column(db.INTEGER, db.ForeignKey('grade.id'), nullable=False)

class Grade(db.Model):
    __tablename__ = 'grade'

    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    g_name = db.Column(db.VARCHAR(32))

