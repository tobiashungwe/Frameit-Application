from quart import Quart, jsonify
from quart_cors import cors
import aiomysql  # Async MySQL library
from services.theme_service import ThemeService  # Import from services folder
from repositories.theme_repository import ThemeRepository  # Import from repositories folder
from models.theme_model import Theme

# Initialize app and CORS
app = Quart(__name__)
app = cors(app, allow_origin="http://localhost:8000")

# Initialize the theme service with the theme repository
theme_repository = ThemeRepository()
theme_service = ThemeService(theme_repository)

# Asynchronous database connection
async def get_db_connection():
    return await aiomysql.connect(
        host='localhost',
        user='root',
        password='root',
        db='theme_database'
    )

# Test database connection
@app.route('/api/test-connection', methods=['GET'])
async def test_connection():
    try:
        connection = await get_db_connection()
        connection.close()
        return jsonify({"status": "Database connected"}), 200
    except Exception as e:
        return jsonify({"status": "Connection failed", "error": str(e)}), 500

# Fetch themes from the service
@app.route("/api/themes/", methods=["GET"])
async def get_themes():
    themes = await theme_service.get_themes()
    return jsonify([theme.to_dict() for theme in themes])

if __name__ == '__main__':
    app.run(debug=True)
