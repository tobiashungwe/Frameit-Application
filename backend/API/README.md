# Theme Data API

## Overview

The Theme Data API provides metadata and content about available themes for front-end components. The API is designed to be extensible for future themes.

## Endpoints

### 1. Get All Themes
**GET** `/api/themes`

**Description:** Returns a list of available themes with metadata.

**Response Example:**
```json
{
  "themes": [
    {
      "name": "Mario",
      "description": "A theme based on the Mushroom Kingdom and Mario's adventures."
    },
    {
      "name": "Pokemon",
      "description": "A theme inspired by the world of Pokemon."
    }
  ]
}
