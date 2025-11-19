from flask_login import UserMixin
from extensions import db, login_manager, bcrypt
from werkzeug.security import check_password_hash as werkzeug_check_password_hash


class User(UserMixin, db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	nome = db.Column(db.String(120), nullable=False)
	email = db.Column(db.String(150), unique=True, nullable=False)
	password_hash = db.Column(db.String(256), nullable=True)
	role = db.Column(db.String(50), default='user')
	ativo = db.Column(db.Boolean, default=True)

	profile = db.relationship(
		'Profile',
		uselist=False,
		back_populates='user',
		cascade='all, delete-orphan',
		passive_deletes=True
	)

	def set_password(self, password: str):
		self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

	def check_password(self, password: str) -> bool:
		if not self.password_hash:
			return False
		if self.password_hash.startswith('pbkdf2:'):
			return werkzeug_check_password_hash(self.password_hash, password)
		if self.password_hash.startswith(('$2a$', '$2b$', '$2y$')):
			try:
				return bcrypt.check_password_hash(self.password_hash, password)
			except ValueError:
				return False
		# fallback attempt for outros formatos legados
		return werkzeug_check_password_hash(self.password_hash, password)

	def get_id(self):
		return str(self.id)



@login_manager.user_loader
def load_user(user_id):
	try:
		return User.query.get(int(user_id))
	except Exception:
		return None
