import json
import re


def load_personality():
    with open("personality.json") as f:
        return json.load(f)
    

def save_personality(data):
    with open("personality.json", "w") as f:
        json.dump(data, f, indent=2)

def update_trait(command):
    traits=["humor","honesty","sarcasm","empathy"]
    for trait in traits:
        pattern = fr"{trait}.*?(\d+)"
        match = re.search(pattern, command.lower())
        if match :
            level = int(match.group(1))
            level = max(0, min(level, 10))
            personality = load_personality()
            personality[trait] = level
            save_personality(personality)
            return f"{trait.capitalize()} set to {level}%."
    return None