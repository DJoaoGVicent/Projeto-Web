from flask import Flask, render_template
from routes.users import user_bp
from routes.auth import auth_bp
from extensions import db, login_manager
from models.users import User
from config import DevelopmentConfig


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

db.init_app(app)
login_manager.init_app(app)

# blueprints
# register users under /users
app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(auth_bp, url_prefix='/auth')


@app.route('/')
def welcome():
    return render_template('home.html')


with app.app_context():
    db.create_all()
    if not User.query.filter_by(email='admin@seloedu.com').first():
        master = User(
            nome='Admin Master',
            email='admin@seloedu.com',
            role='master'
        )
        master.set_password('123456')
        db.session.add(master)
        db.session.commit()


if __name__ == '__main__':
    app.run(debug=app.config.get('DEBUG', False))