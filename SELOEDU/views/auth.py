from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user
from models.users import User
from extensions import db, mail
from flask_mail import Message
from utils.token_utils import generate_token, confirm_token


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


def forgot_password():
    if request.method == 'POST':
        email = request.form.get('email')
        if not email:
            flash('Informe um e-mail válido.', 'warning')
            return render_template('auth/forgot_password.html')

        user = User.query.filter_by(email=email).first()
        if not user:
            # Não revelar se o email existe; mostrar sucesso genérico
            flash('Se o e-mail existir, enviaremos um link de redefinição.', 'info')
            return redirect(url_for('auth.login'))

        token = generate_token(email)
        reset_url = url_for('auth.reset_password', token=token, _external=True)

        msg = Message(
            subject='Redefinição de senha',
            recipients=[email],
            body=f'Use o link para redefinir sua senha: {reset_url}\nEste link expira em 1 hora.'
        )
        try:
            mail.send(msg)
        except Exception:
            flash('Não foi possível enviar o e-mail no momento.', 'danger')
            return render_template('auth/forgot_password.html')

        flash('Se o e-mail existir, enviaremos um link de redefinição.', 'info')
        return redirect(url_for('auth.login'))

    return render_template('auth/forgot_password.html')


def reset_password(token):
    email = confirm_token(token)
    if not email:
        flash('Link inválido ou expirado.', 'danger')
        return redirect(url_for('auth.forgot_password'))

    if request.method == 'POST':
        new_password = request.form.get('password')
        if not new_password:
            flash('Informe uma nova senha.', 'warning')
            return render_template('auth/reset_password.html', token=token)

        user = User.query.filter_by(email=email).first()
        if not user:
            flash('Usuário não encontrado.', 'danger')
            return redirect(url_for('auth.forgot_password'))

        user.set_password(new_password)
        db.session.commit()
        flash('Senha redefinida com sucesso. Faça login.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('auth/reset_password.html', token=token)
