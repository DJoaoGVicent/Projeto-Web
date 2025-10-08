from flask import Flask, render_template
from routes.user import user_bp
from routes.auth import auth_bp
from models.extensions import db, login_manager
from models.user import User
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET', 'dev-secret')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///seloedu.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)
login_manager.init_app(app)

# blueprints
app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(auth_bp, url_prefix='/auth')


@app.route('/')
def welcome():
    return render_template('home.html')

#Criar master para a database
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
    app.run(debug=True)