import requests
from bs4 import BeautifulSoup
import json
import re
import os

# List of Wikipedia URLs for character or game themes
urls = [
    "https://en.wikipedia.org/wiki/Mario",
    "https://en.wikipedia.org/wiki/Halloween",
    "https://en.wikipedia.org/wiki/Fortnite",
    "https://en.wikipedia.org/wiki/Christmas",
]

# Directory to save the JSON data file
data_dir = os.path.join(os.path.dirname(__file__), "../data")
os.makedirs(data_dir, exist_ok=True)
json_file_path = os.path.join(data_dir, "theme_data.json")


def scrape_theme_data(url):
    """
    Scrapes data from a Wikipedia page, focusing on main content paragraphs.
    Cleans text and organizes it by theme.
    """
    response = requests.get(url)
    response.raise_for_status()  # Check for request errors
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract the theme or character name from the page title
    theme_name = soup.find("h1", id="firstHeading").text

    # Extract the main content of the page (e.g., introduction and summary sections)
    paragraphs = soup.select("div.mw-parser-output > p")
    content = []
    for para in paragraphs:
        text = para.get_text()
        if text.strip():  # Ignore empty paragraphs
            # Clean the text: remove citations (like [1], [2], etc.)
            text = re.sub(r"\[\d+\]", "", text)
            content.append(text)

    # Join all text paragraphs to form a single narrative
    description = " ".join(content)

    # Structure the data
    theme_data = {
        "theme_name": theme_name,
        "description": description,
        "source_url": url,
    }

    return theme_data


def main():
    """
    Main function to scrape data from all URLs, organize it, and save to JSON.
    """
    all_theme_data = []
    for url in urls:
        try:
            theme_data = scrape_theme_data(url)
            all_theme_data.append(theme_data)
            print(f"Successfully scraped data for: {theme_data['theme_name']}")
        except Exception as e:
            print(f"Failed to scrape {url}: {e}")

    # Save the collected data to a JSON file
    with open(json_file_path, "w") as f:
        json.dump(all_theme_data, f, indent=4)
        print(f"Data saved to {json_file_path}")


if __name__ == "__main__":
    main()
