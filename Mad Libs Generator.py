# Story Template
story = """Once upon a time, there was a brave {noun_singular} named {noun_plural} who lived in a {adjective1} {noun2}. One day, {noun_plural} went on a quest to find the {noun_singular} {noun3}. Along the way, they encountered a {adjective2} {noun4} who offered them a {adjective3} {noun5}. {noun_plural} accepted the gift and continued their journey. Finally, {noun_plural} reached the {place}, but it was guarded by a {adjective4} {noun6}! {noun_plural} used their {ability} {noun_singular} to defeat the beast and claim the {adjective5} {noun3}. They returned home a hero, forever known as the {title} of the {place2}."""

parts_of_speech = {
    "noun_singular": "noun (singular)",
    "noun_plural": "noun (plural)",
    "adjective1": "adjective",
    "adjective2": "adjective",
    "verb_past_tense1": "verb (past tense)",
    "noun2": "noun",
    "adjective3": "adjective",
    "noun3": "noun",
    "adjective4": "adjective",
    "noun4": "noun",
    "verb_past_tense2": "verb (past tense)",
    "noun5": "noun",
    "place": "place",
    "adjective5": "adjective",
    "noun6": "noun",
    "ability": "ability",
    "adjective6": "adjective",
    "title": "title",
    "place2": "place",
}

user_inputs = {}
for part, options in parts_of_speech.items():
    print(f"Enter a {options}: ")
    user_inputs[part] = input()

# Replace placeholders with input
completed_story = story.format(**user_inputs)

print("\nYour Mad Lib:\n")
print(completed_story)
