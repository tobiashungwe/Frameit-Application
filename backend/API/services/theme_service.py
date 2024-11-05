class ThemeService:
    def __init__(self, theme_repository):
        self.theme_repository = theme_repository

    def get_themes(self):
        return self.theme_repository.get_all_themes()
