# knowledge.py

OBJECTS_DB = {
    "earth": {
        "name": "Planet Earth",
        "short_intro": "This is planet Earth, the third planet from the Sun.",
        "details": """
Earth is the only known planet to support life. About 71 percent of its surface is covered by water.
It has one natural satellite, the Moon, and an atmosphere that protects life and keeps temperatures relatively stable.
"""
    },
    "human_heart": {
        "name": "Human Heart",
        "short_intro": "This is the human heart, the organ that pumps blood through your body.",
        "details": """
The heart is a muscular organ with four chambers: left atrium, right atrium, left ventricle, and right ventricle.
It circulates blood through the lungs to pick up oxygen and then pumps it to the rest of the body.
"""
    },
    # You can add more objects here later
}

def get_object_info(object_id: str):
    return OBJECTS_DB.get(object_id)
    