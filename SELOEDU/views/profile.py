from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from models.profile import Profile
from extensions import db

@login_required
def profile():
    profile = Profile.query.filter_by(user_id=current_user.id).first()
    if request.method == 'POST':
        telefone = request.form.get('telefone')
        instituicao = request.form.get('instituicao')
        cargo = request.form.get('cargo')
        bio = request.form.get('bio')
        foto = request.files.get('foto')
        
        if not profile:
            profile = Profile(user_id=current_user.id)
            db.session.add(profile)
        profile.telefone = telefone
        profile.instituicao = instituicao
        profile.cargo = cargo
        profile.bio = bio
        if foto and foto.filename:
            # Salvar o arquivo de foto (ajuste o caminho conforme necessário)
            foto_path = f'static/uploads/{current_user.id}_{foto.filename}'
            foto.save(foto_path)
            profile.foto = foto_path
        db.session.commit()
        flash('Perfil atualizado com sucesso!', 'success')
        return redirect(url_for('users.profile'))
    return render_template('users/profile.html', profile=profile)
