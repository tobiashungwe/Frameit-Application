import mysql.connector
from config import Config
from models.theme_model import Theme


class ThemeRepository:
    def __init__(self):
        self.connection = None

    def _get_connection(self):
        if self.connection is None or not self.connection.is_connected():
            self.connection = mysql.connector.connect(
                host=Config.MYSQL_HOST,
                user=Config.MYSQL_USER,
                password=Config.MYSQL_PASSWORD,
                database=Config.MYSQL_DB
            )
        return self.connection

    def get_all_themes(self):
        conn = self._get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, name FROM themes")
        themes = [Theme(row['id'], row['name']) for row in cursor.fetchall()]
        cursor.close()
        return themes

    def __del__(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
