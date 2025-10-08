from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from extensions import db, login_manager


class User(UserMixin, db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	nome = db.Column(db.String(120), nullable=False)
	email = db.Column(db.String(150), unique=True, nullable=False)
	password_hash = db.Column(db.String(256), nullable=True)
	role = db.Column(db.String(50), default='user')
	ativo = db.Column(db.Boolean, default=True)

	def set_password(self, password: str):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password: str) -> bool:
		if not self.password_hash:
			return False
		return check_password_hash(self.password_hash, password)

	def get_id(self):
		return str(self.id)



@login_manager.user_loader
def load_user(user_id):
	try:
		return User.query.get(int(user_id))
	except Exception:
		return None
