# voicebot/tts.py
import pyttsx3

def _create_engine():
    # Explicitly use Windows SAPI5 driver
    engine = pyttsx3.init(driverName="sapi5")
    engine.setProperty("rate", 175)   # speaking speed
    engine.setProperty("volume", 1.0) # 0.0 to 1.0
    return engine


def speak(text: str):
    """
    More robust TTS:
    - Creates a fresh engine each call (avoids 'stuck' engine issues)
    - Normalizes whitespace
    - Optionally could chunk text if it's huge
    """
    if not text:
        return

    # Debug print so we see every call
    print(f"[TTS] {text}")

    # Normalize text (remove excessive newlines/spaces)
    cleaned = " ".join(str(text).split())

    engine = _create_engine()
    engine.say(cleaned)
    engine.runAndWait()
    engine.stop()
