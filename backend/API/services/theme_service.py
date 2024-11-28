class ThemeService:
    def __init__(self, theme_repository):
        self.theme_repository = theme_repository

    async def get_themes(self):
        return await self.theme_repository.get_all_themes()
