from flask import Flask, request, render_template, redirect, url_for, Blueprint, jsonify
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)
db = SQLAlchemy(app)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    faculty = db.Column(db.String(50), nullable=False)


with app.app_context():
    db.create_all()

students_bp = Blueprint('students', __name__)
api_students = Api(students_bp)


class StudentResource(Resource):
    def get(self, student_id):
        student = Student.query.get_or_404(student_id)
        return {'id': student.id, 'name': student.name, 'age': student.age, 'faculty': student.faculty}

    def put(self, student_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, help='Name cannot be blank')
        parser.add_argument('age', type=int, required=True, help='Age cannot be blank')
        parser.add_argument('faculty', type=str, required=True, help='Faculty cannot be blank')

        args = parser.parse_args()
        student = Student.query.get_or_404(student_id)
        student.name = args['name']
        student.age = args['age']
        student.faculty = args['faculty']
        db.session.commit()
        return {'message': 'Student updated successfully'}

    def delete(self, student_id):
        student = Student.query.get_or_404(student_id)
        db.session.delete(student)
        db.session.commit()
        return {'message': 'Student deleted successfully'}


class StudentsResource(Resource):
    def get(self):
        students = Student.query.all()
        students_data = [{'id': student.id, 'name': student.name, 'age': student.age, 'faculty': student.faculty} for student in students]
        return jsonify(students_data)

    def post(self):
        try:
            if request.content_type == 'application/json':
                data = request.get_json()
            else:
                data = request.form
            if 'name' not in data or 'age' not in data or 'faculty' not in data:
                return {'message': 'Missing required data'}, 400
            new_student = Student(name=data['name'], age=data['age'], faculty=data['faculty'])
            db.session.add(new_student)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            return {'message': str(e)}, 500


api_students.add_resource(StudentResource, '/student/<int:student_id>')
api_students.add_resource(StudentsResource, '/students', endpoint='students')


@students_bp.route('/')
def get_students():
    students = Student.query.all()
    return render_template('index.html', students=students)


@students_bp.route('/delete/<int:student_id>', methods=['GET'])
def delete_student(student_id):
    student = Student.query.get_or_404(student_id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for('students.get_students'))


@students_bp.route('/update/<int:student_id>', methods=['GET', 'POST'])
def update_student(student_id):
    student = Student.query.get_or_404(student_id)

    if request.method == 'POST':
        student.name = request.form['name']
        student.age = request.form['age']
        student.faculty = request.form['faculty']
        db.session.commit()
        return redirect(url_for('students.get_students'))

    return render_template('edit_student.html', student=student)


app.register_blueprint(students_bp)

if __name__ == '__main__':
    app.run(debug=True)
