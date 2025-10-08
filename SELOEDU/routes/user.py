from flask import Blueprint
from flask_login import login_required
from views import users as users_views

user_bp = Blueprint('users', __name__, template_folder='templates')

'''
@user_bp.route('/')
@login_required
def index():
    # simple dashboard redirect to protected dashboard
    return redirect(url_for('users_views.dashboard'))
'''

@user_bp.route('/settings')
@login_required
def settings():
    return users_views.settings()

@user_bp.route('/dashboard')
@login_required
def dashboard():
    return users_views.dashboard()

@user_bp.route('/users')
@login_required
def users():
    return users_views.users()

'''
@user_bp.before_request
def ensure_authenticated():
    # login_required decorators already enforce auth, but keep hook for extra checks
    pass
'''
