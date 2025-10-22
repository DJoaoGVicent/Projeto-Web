from flask import Blueprint
from views import auth as auth_views

auth_bp = Blueprint('auth', __name__, template_folder='templates')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    return auth_views.login()


@auth_bp.route('/logout')
def logout():
    return auth_views.logout()


@auth_bp.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    return auth_views.forgot_password()


@auth_bp.route('/reset-password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    return auth_views.reset_password(token)