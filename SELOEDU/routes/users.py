from flask import Blueprint
from flask_login import login_required
from views import users as users_views
from views.profile import profile

user_bp = Blueprint('users', __name__, template_folder='templates')

# Instanciar a view
user_view = users_views.UserView()

# Rotas (definindo endpoints amigáveis usados pelos templates)
user_bp.route('/', endpoint='index', methods=['GET'])(user_view.list_users)
user_bp.route('/create', endpoint='create', methods=['GET', 'POST'])(user_view.create_user)
user_bp.route('/<int:user_id>', endpoint='show', methods=['GET'])(user_view.view_user)
user_bp.route('/<int:user_id>/edit', endpoint='edit', methods=['GET', 'POST'])(user_view.edit_user)
user_bp.route('/<int:user_id>/delete', endpoint='delete', methods=['POST'])(user_view.delete_user)
user_bp.route('/profile', endpoint='profile', methods=['GET', 'POST'])(profile)

@user_bp.route('/settings', endpoint='settings')
@login_required
def settings():
    return users_views.settings()


@user_bp.route('/dashboard', endpoint='dashboard')
@login_required
def dashboard():
    return users_views.dashboard()
