from flask import Blueprint, request, jsonify
from .extensions import db, bcrypt
from .models import User, Course, ContactMessage
from .forms import RegistrationForm, LoginForm, ContactForm
from flask_login import login_user, logout_user, login_required

bp = Blueprint('routes', __name__)

@bp.route('/')
def home():
    return "Welcome to the Cluster Classes backend!"

@bp.route('/register', methods=['POST'])
def register():
    form = RegistrationForm(data=request.get_json())
    if form.validate():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password_hash=hashed_password)
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully!'}), 201
    return jsonify({'errors': form.errors}), 400

@bp.route('/login', methods=['POST'])
def login():
    form = LoginForm(data=request.get_json())
    if form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password_hash, form.password.data):
            login_user(user, remember=form.remember.data)
            return jsonify({'message': 'Login successful!'})
        else:
            return jsonify({'message': 'Login Unsuccessful. Please check email and password'}), 401
    return jsonify({'errors': form.errors}), 400

@bp.route('/logout')
def logout():
    logout_user()
    return jsonify({'message': 'Logout successful!'})

@bp.route('/contact', methods=['POST'])
def contact():
    form = ContactForm(data=request.get_json())
    if form.validate():
        message = ContactMessage(name=form.name.data, email=form.email.data, message=form.message.data)
        db.session.add(message)
        db.session.commit()
        return jsonify({'message': 'Message sent successfully!'}), 201
    return jsonify({'errors': form.errors}), 400

# Course Management Routes
@bp.route('/courses', methods=['GET'])
def get_courses():
    courses = Course.query.all()
    return jsonify([{'id': c.id, 'title': c.title, 'description': c.description, 'category': c.category} for c in courses])

@bp.route('/courses', methods=['POST'])
@login_required
def create_course():
    data = request.get_json()
    if not data or not 'title' in data or not 'description' in data or not 'category' in data:
        return jsonify({'message': 'Invalid data'}), 400

    new_course = Course(title=data['title'], description=data['description'], category=data['category'])
    db.session.add(new_course)
    db.session.commit()

    return jsonify({'message': 'Course created successfully', 'id': new_course.id}), 201

@bp.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    course = Course.query.get_or_404(course_id)
    return jsonify({'id': course.id, 'title': course.title, 'description': course.description, 'category': course.category})

@bp.route('/courses/<int:course_id>', methods=['PUT'])
@login_required
def update_course(course_id):
    course = Course.query.get_or_404(course_id)
    data = request.get_json()

    course.title = data.get('title', course.title)
    course.description = data.get('description', course.description)
    course.category = data.get('category', course.category)

    db.session.commit()
    return jsonify({'message': 'Course updated successfully'})

@bp.route('/courses/<int:course_id>', methods=['DELETE'])
@login_required
def delete_course(course_id):
    course = Course.query.get_or_404(course_id)
    db.session.delete(course)
    db.session.commit()
    return jsonify({'message': 'Course deleted successfully'})