from repositories.theme_repository import ThemeRepository
from services.theme_service import ThemeService

# Dependency Injection setup
theme_repository = ThemeRepository()
theme_service = ThemeService(theme_repository)
