from flask import Blueprint
from views.treinamento_view import TreinamentoView


treinamento_bp = Blueprint('treinamento', __name__, template_folder='templates')

view = TreinamentoView()

treinamento_bp.add_url_rule('/', view_func=view.listar, methods=['GET'], endpoint='listar')
treinamento_bp.add_url_rule('/novo', view_func=view.novo, methods=['GET', 'POST'], endpoint='novo')


