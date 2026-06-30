# intent.py
from knowledge import OBJECTS_DB

OBJECT_ALIASES = {
    "earth": ["earth", "planet earth"],
    "human_heart": ["heart", "human heart", "the heart"],
    # add more if you add objects
}

COMMAND_WORDS = ["show", "display", "project", "open"]


def detect_display_command(user_text: str):
    text = user_text.lower()

    if not any(w in text for w in COMMAND_WORDS):
        return None

    for obj_id, aliases in OBJECT_ALIASES.items():
        for alias in aliases:
            if alias in text:
                return obj_id

    return None


def list_known_objects() -> str:
    names = [f"- {data['name']}" for _, data in OBJECTS_DB.items()]
    return "\n".join(names)
