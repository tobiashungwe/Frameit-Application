from dataclasses import dataclass


@dataclass
class ThemeDependencies:
    """Dependencies for theme-based tools."""

    theme: str
    # activity_description: str
    # user_keywords: list[str]


@dataclass
class ResearchDependencies:
    """Dependencies for researching a theme and related keywords."""

    theme: str
    user_keywords: list[str]


@dataclass
class AdapterDependencies:
    """Dependencies for mapping objects to a theme."""

    theme: str
    activity_description: str
    user_keywords: list[str]


@dataclass
class TranslationDependencies:
    """Dependencies for translating a story."""

    story: str
    target_language: str
