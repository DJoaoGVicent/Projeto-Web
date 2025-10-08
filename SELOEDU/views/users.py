from flask import render_template
from models.user import User


def dashboard():
    return render_template('dashboard.html')

def users():
    try:
        usuarios = User.query.all()
    except Exception:
        usuarios = []
    return render_template('users.html', usuarios=usuarios)

def settings():
    return render_template('dashboard.html')  # temporario
