from flask import Blueprint, jsonify
from main import theme_service


theme_blueprint = Blueprint('theme_controller', __name__)


@theme_blueprint.route('/', methods=['GET'])
def get_themes():
    themes = theme_service.get_themes()
    return jsonify([theme.to_dict() for theme in themes])
