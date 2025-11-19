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
    def redirect_current_context():
        if user_id is not None:
            return redirect(url_for('users.profile_user', user_id=target_user_id))
        return redirect(url_for('users.profile'))

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
                return redirect_current_context()

            old_filename = profile.foto
            old_thumb = profile.foto_thumb
            saved_filename, thumb_filename = save_image(file_storage=foto, user_name=subject_user.nome)
            if not saved_filename and not thumb_filename:
                flash('Não foi possível salvar a imagem.', 'danger')
                return redirect_current_context()

            # Se for GIF, usar o arquivo original para preservar animação; senão preferir thumbnail
            is_gif = (saved_filename or '').lower().endswith('.gif')
            if is_gif:
                profile.foto = saved_filename
                profile.foto_thumb = None
            else:
                profile.foto = saved_filename
                profile.foto_thumb = thumb_filename

            # limpar arquivos antigos
            if old_filename:
                try:
                    remove_file_safe(old_filename)
                except Exception:
                    pass
            if old_thumb:
                try:
                    remove_file_safe(old_thumb)
                except Exception:
                    pass
        db.session.commit()
        flash('Perfil atualizado com sucesso!', 'success')
        # redireciona permanecendo na página correta (self ou outro)
        return redirect_current_context()
    return render_template('users/profile.html', profile=profile, subject_user=subject_user)
