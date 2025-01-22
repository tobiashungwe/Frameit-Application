from dataclasses import dataclass
from typing import List


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
    exercise: str
    user_keywords: list[str]
    materials: list[str]


@dataclass
class GeneratorDependencies:
    """Dependencies for generating a story."""

    theme: str
    exercise: str
    theme_details: List[str]
    object_mapping: List[str]


@dataclass
class TranslationDependencies:
    """Dependencies for translating a story."""

    story: str
    target_language: str


# Define dependencies for the Editor Agent
@dataclass
class EditorDependencies:
    """Dependencies for refining a story."""

    story: str
