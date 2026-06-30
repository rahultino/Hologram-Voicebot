# hologram.py
from knowledge import get_object_info

def project_object(object_id: str):
    info = get_object_info(object_id)
    if info:
        print(f"[HOLOGRAM] Displaying: {info['name']} (id={object_id})")
        # TODO: replace this print with real hologram control on Raspberry Pi
    else:
        print(f"[HOLOGRAM] Unknown object id={object_id}")
