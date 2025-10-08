from flask import render_template, request, redirect, url_for, flash, jsonify
from models.users import User
from extensions import db


def dashboard():
    return render_template('dashboard.html')


def settings():
    return render_template('dashboard.html')  # temporario

class UserView:
    def list_users(self):
        """Listar todos os usuários"""
        try:
            users = User.query.filter_by(ativo=True).all()
            # templates expect the variable name 'usuarios'
            return render_template('users/index.html', usuarios=users)
        except Exception as e:
            flash(f'Erro ao carregar usuários: {str(e)}', 'error')
            return render_template('users/index.html', usuarios=[])
    
    def create_user(self):
        """Criar novo usuário"""
        if request.method == 'POST':
            try:
                nome = request.form.get('nome')
                email = request.form.get('email')
                password = request.form.get('password')
                # use the Portuguese default role used in templates
                role = request.form.get('role', 'aluno')

                # Validar dados
                if not nome or not email:
                    flash('Nome e email são obrigatórios', 'error')
                    # pass form data back so template can pre-fill fields
                    return render_template('users/form.html', form_data=request.form)

                # Verificar se email já existe
                if User.query.filter_by(email=email).first():
                    flash('Email já cadastrado', 'error')
                    return render_template('users/form.html', form_data=request.form)

                # Criar usuário
                user = User(
                    nome=nome,
                    email=email,
                    role=role
                )
                if password:
                    user.set_password(password)

                db.session.add(user)
                db.session.commit()

                flash('Usuário criado com sucesso!', 'success')
                return redirect(url_for('users.index'))

            except Exception as e:
                db.session.rollback()
                flash(f'Erro ao criar usuário: {str(e)}', 'error')
                return render_template('users/form.html', form_data=request.form)

        return render_template('users/form.html')
    
    def view_user(self, user_id):
        """Visualizar usuário específico"""
        try:
            user = User.query.get_or_404(user_id)
            return render_template('users/show.html', user=user)
        except Exception as e:
            flash(f'Erro ao carregar usuário: {str(e)}', 'error')
            return redirect(url_for('users.index'))
    
    def edit_user(self, user_id):
        """Editar usuário"""
        user = User.query.get_or_404(user_id)
        
        if request.method == 'POST':
            try:
                user.nome = request.form.get('nome', user.nome)
                user.email = request.form.get('email', user.email)
                user.role = request.form.get('role', user.role)

                password = request.form.get('password')
                if password:
                    user.set_password(password)

                db.session.commit()
                flash('Usuário atualizado com sucesso!', 'success')
                return redirect(url_for('users.show', user_id=user.id))

            except Exception as e:
                db.session.rollback()
                flash(f'Erro ao atualizar usuário: {str(e)}', 'error')

        return render_template('users/form.html', user=user)
    
    def delete_user(self, user_id):
        """Excluir usuário (soft delete)"""
        try:
            user = User.query.get_or_404(user_id)
            user.ativo = False
            db.session.commit()
            flash('Usuário excluído com sucesso!', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Erro ao excluir usuário: {str(e)}', 'error')
        
        return redirect(url_for('users.index'))