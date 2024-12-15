from dataclasses import dataclass
from typing import List


@dataclass
class ThemeDependencies:
    theme: str
    activity_description: str
    user_keywords: List[str]
