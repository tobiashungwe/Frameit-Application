import aiomysql
from models.theme_model import Theme
from config import Config

class ThemeRepository:
    def __init__(self):
        self.connection = None

    async def _get_connection(self):
        if self.connection is None or not self.connection.open:
            self.connection = await aiomysql.connect(
                host=Config.MYSQL_HOST,
                user=Config.MYSQL_USER,
                password=Config.MYSQL_PASSWORD,
                db=Config.MYSQL_DB,
            )
        return self.connection

    async def get_all_themes(self):
        conn = await self._get_connection()
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            await cursor.execute("SELECT id, name, description FROM themes")
            result = await cursor.fetchall()
            themes = [Theme(row["id"], row["name"], row["description"]) for row in result]
        return themes
