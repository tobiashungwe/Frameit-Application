from typing import List, Dict
import requests


# Curator Agent: Suggests themes and related keywords
class Curator:
    def suggest_themes(self) -> List[str]:
        # Replace with actual logic or API calls
        # connection with the databse using api call
        # Todo: Recommend themes that are popular or trending

        # you can only choose one theme at at time, cofirmed button should prevent this problem
        return ["Mario", "Minions", "Brawl Stars", "Christmas", "Halloween"]

    def suggest_related_keywords(self, theme: str) -> List[str]:
        # Replace with actual logic or API calls
        if theme.lower() == "mario":
            return ["Luigi", "Peach", "Mushrooms", "Warp Pipe", "Koopas"]
        return []


# Search agent:Searches teams if not found in the list
class SearchAgent:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.search_url = "https://api.search.brave.com/v1/search"

    def fetch_information(self, query: str) -> Dict:
        headers = {
            "Accept": "application/json",
            "X-Subscription-Token": self.api_key,
        }
        params = {
            "q": query,
            "count": 5,  # Number of search results to retrieve
        }
        response = requests.get(self.search_url, headers=headers, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()


# Researcher Agent: Retrieves detailed information about the theme
class Researcher:
    def get_theme_info(self, theme: str) -> Dict[str, List[str]]:
        # Replace with actual logic or API calls

        # Words that are generated,should be the final words
        if theme.lower() == "mario":
            return {
                "characters": ["Mario", "Luigi", "Princess Peach"],
                "items": ["mushrooms", "warp pipes", "fire flowers"],
                "enemies": ["Goombas", "Koopas"],
                "settings": ["Mushroom Kingdom"],
            }
        return {}


# Adapter Agent: Maps generic activity objects to theme-specific equivalents
class Adapter:
    def map_objects(
        self, activity_objects: List[str], theme_info: Dict[str, List[str]]
    ) -> Dict[str, str]:
        # Replace with actual logic or API calls
        mapping = {}
        for obj in activity_objects:
            if obj == "tunnel":
                mapping[obj] = "warp pipe"
            elif obj == "ball":
                mapping[obj] = "Koopa shell"
            else:
                mapping[obj] = obj
        return mapping


# Generator Agent: Creates a story based on the activity and theme information
class Generator:
    def create_story(
        self,
        activity_description: str,
        theme_info: Dict[str, List[str]],
        object_mapping: Dict[str, str],
        user_keywords: List[str],
    ) -> str:
        # Replace with actual logic or API calls
        story = f"In the {theme_info.get('settings', ['unknown'])[0]}, "
        story += f"{', '.join(theme_info.get('characters', ['someone']))} were "
        story += f"{activity_description}, using {', '.join(object_mapping.values())}. "
        story += (
            f"They encountered {', '.join(theme_info.get('enemies', ['no enemies']))}."
        )
        return story


# Todo: editor agent: Can edit specific lines of text that was generarated (Nice to have)
