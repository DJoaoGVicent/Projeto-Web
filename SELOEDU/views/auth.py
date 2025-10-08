from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user
from models.users import User
from extensions import db


def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)
            flash('Login realizado com sucesso.', 'success')
            return redirect(url_for('users.dashboard'))
        flash('Credenciais inválidas.', 'danger')
        return render_template('auth/login.html')

    return render_template('auth/login.html')


def logout():
    logout_user()
    flash('Você foi desconectado.', 'info')
    return redirect(url_for('auth.login'))
