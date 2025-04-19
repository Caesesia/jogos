import json

# Open and load the JSON file
with open("data/scenes.json", "r", encoding="utf-8") as file:
    story = json.load(file)

# Print the synopsis
print(story["synopsis"], story["persos"], story["fin"])

