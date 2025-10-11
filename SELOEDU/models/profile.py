from extensions import db

class Profile(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    telefone = db.Column(db.String(20))
    instituicao = db.Column(db.String(100))
    cargo = db.Column(db.String(100))
    foto = db.Column(db.String(255))
    bio = db.Column(db.Text)

    user = db.relationship('User', back_populates='profile')
