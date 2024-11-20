import json
import os

# Dynamically construct the path to the data file
script_dir = os.path.dirname(__file__)  # Get the directory of the current script
data_path = os.path.join(script_dir, '../data/theme_data.json')  # Navigate to the data directory

# Load your scraped data (with utf-8 encoding to avoid encoding errors)
with open(data_path, 'r', encoding='utf-8') as f:
    theme_data = json.load(f)

# Prepare data for fine-tuning
# Example format: "<theme_name>: <description>"
training_texts = [f"{item['theme_name']}: {item['description']}" for item in theme_data]

# Save the prepared texts into a plain text file (with utf-8 encoding to avoid encoding errors)
output_file_path = os.path.join(script_dir, '../data/theme_training.txt')

with open(output_file_path, 'w', encoding='utf-8') as f:  # Specify utf-8 encoding
    f.write("\n\n".join(training_texts))

print(f"Training data written to: {output_file_path}")