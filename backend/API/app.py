from flask import Flask
from flask_cors import CORS
from controllers.theme_controller import theme_blueprint
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:8000"}})

# Register blueprints
app.register_blueprint(theme_blueprint, url_prefix='/api/themes')

if __name__ == '__main__':
    app.run(debug=True)
