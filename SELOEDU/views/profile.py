from flask import render_template, request, redirect, url_for, flash, current_app
from flask_login import login_required, current_user
from models.profile import Profile
from models.users import User
from extensions import db
from utils.uploads import save_image, remove_file_safe

@login_required
def profile(user_id=None):
    # Determina o usuário alvo (self ou outro). Apenas 'master' pode editar terceiros.
    target_user_id = current_user.id
    if user_id is not None and user_id != current_user.id:
        if current_user.role != 'master':
            flash('Acesso negado. Apenas usuários master podem editar perfis de terceiros.', 'danger')
            return redirect(url_for('users.show', user_id=user_id))
        target_user_id = user_id

    subject_user = User.query.get_or_404(target_user_id)
    profile = Profile.query.filter_by(user_id=target_user_id).first()
    if request.method == 'POST':
        telefone = request.form.get('telefone')
        instituicao = request.form.get('instituicao')
        cargo = request.form.get('cargo')
        bio = request.form.get('bio')
        foto = request.files.get('foto')
        
        if not profile:
            profile = Profile(user_id=target_user_id)
            db.session.add(profile)
        profile.telefone = telefone
        profile.instituicao = instituicao
        profile.cargo = cargo
        profile.bio = bio
        if foto and foto.filename:
            filename_lower = (foto.filename or '').lower()
            if '.' in filename_lower:
                ext = filename_lower.rsplit('.', 1)[-1]
            else:
                ext = ''
            allowed = current_app.config.get('ALLOWED_IMAGE_EXTENSIONS', {"png","jpg","jpeg","gif"})
            if ext not in allowed:
                flash('Formato de imagem não permitido.', 'warning')
                return redirect(url_for('users.profile'))

            old_filename = profile.foto if getattr(profile, 'foto', None) else None
            saved_filename, thumb_filename = save_image(file_storage=foto, user_name=subject_user.nome)
            if not saved_filename and not thumb_filename:
                flash('Não foi possível salvar a imagem.', 'danger')
                return redirect(url_for('users.profile'))

            # Se for GIF, usar o arquivo original para preservar animação; senão preferir thumbnail
            is_gif = (saved_filename or '').lower().endswith('.gif')
            profile.foto = (saved_filename if is_gif else (thumb_filename or saved_filename))

            # limpar arquivos antigos
            if old_filename:
                try:
                    remove_file_safe(old_filename)
                    remove_file_safe(f"thumb_{old_filename}")
                except Exception:
                    pass
        db.session.commit()
        flash('Perfil atualizado com sucesso!', 'success')
        # redireciona permanecendo na página correta (self ou outro)
        if user_id is not None:
            return redirect(url_for('users.profile_user', user_id=target_user_id))
        return redirect(url_for('users.profile'))
    return render_template('users/profile.html', profile=profile, subject_user=subject_user)
