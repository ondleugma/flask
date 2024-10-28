from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydat    """  """abase.db'
db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    middle_name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    salary = db.Column(db.Float, nullable=False)
    address = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<Студент: {self.first_name} {self.last_name}>'

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    middle_name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    salary = db.Column(db.Float, nullable=False)
    address = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<Student {self.first_name} {self.last_name}>'

class Prepod(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    middle_name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    salary = db.Column(db.Float, nullable=False)
    address = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<Преподаватель: {self.first_name} {self.last_name}>'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/students')
def students():
    page = request.args.get('page', 1, type=int)
    students = Student.query.paginate(page=page, per_page=5)
    return render_template('students.html', students=students)


@app.route('/prepods')
def prepods():
    page = request.args.get('page', 1, type=int)
    prepods = Prepod.query.paginate(page=page, per_page=5)
    return render_template('prepods.html', prepods=prepods)

if __name__ == '__main__':
    app.run(debug=True, port=8001)