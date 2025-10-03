from flask import Flask, request, jsonify
from .extensions import db, migrate, bcrypt, login_manager, cors
from .models import User, Course, ContactMessage

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI='sqlite:///site.db',
        WTF_CSRF_ENABLED=False
    )

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    cors.init_app(app)

    login_manager.login_view = 'login'
    login_manager.login_message_category = 'info'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    with app.app_context():
        from . import routes
        app.register_blueprint(routes.bp)

        # Create database tables if they don't exist
        db.create_all()

    return app