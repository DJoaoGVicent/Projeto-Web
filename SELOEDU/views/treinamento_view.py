from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from models.treinamento import Treinamento
from extensions import db
from datetime import datetime


class TreinamentoView:
	@login_required
	def listar(self):
		itens = Treinamento.query.order_by(Treinamento.id.desc()).all()
		return render_template('treinamento/listar.html', itens=itens)

	@login_required
	def novo(self):
		if current_user.role != 'coordenador':
			flash('Apenas usuários com papel coordenador podem cadastrar treinamentos.', 'danger')
			return redirect(url_for('treinamento.listar'))

		if request.method == 'POST':
			titulo = request.form.get('titulo')
			descricao = request.form.get('descricao')
			data_inicio_str = request.form.get('data_inicio')
			data_fim_str = request.form.get('data_fim')

			if not titulo:
				flash('Título é obrigatório.', 'warning')
				return render_template('treinamento/novo.html', form_data=request.form)

			def parse_date(s):
				try:
					return datetime.strptime(s, '%Y-%m-%d').date() if s else None
				except Exception:
					return None

			data_inicio = parse_date(data_inicio_str)
			data_fim = parse_date(data_fim_str)

			item = Treinamento(
				titulo=titulo,
				descricao=descricao,
				data_inicio=data_inicio,
				data_fim=data_fim,
			)
			try:
				db.session.add(item)
				db.session.commit()
				flash('Treinamento cadastrado com sucesso.', 'success')
				return redirect(url_for('treinamento.listar'))
			except Exception as e:
				db.session.rollback()
				flash(f'Erro ao salvar treinamento: {str(e)}', 'danger')
				return render_template('treinamento/novo.html', form_data=request.form)

		return render_template('treinamento/novo.html')


