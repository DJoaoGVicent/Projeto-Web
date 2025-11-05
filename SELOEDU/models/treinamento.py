from extensions import db


class Treinamento(db.Model):
	__tablename__ = 'treinamentos'
	id = db.Column(db.Integer, primary_key=True)
	titulo = db.Column(db.String(200), nullable=False)
	descricao = db.Column(db.Text, nullable=True)
	data_inicio = db.Column(db.Date, nullable=True)
	data_fim = db.Column(db.Date, nullable=True)


