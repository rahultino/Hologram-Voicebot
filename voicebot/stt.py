# voicebot/stt.py

import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import tempfile
from groq import Groq

client = Groq()  # uses GROQ_API_KEY


def listen_text():
    """
    Records a short audio clip from the microphone
    and sends it to Groq Whisper for STT.
    """

    print("\n🎤 Listening... Speak now.")
    duration = 6  # seconds
    sample_rate = 16000

    recording = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="int16"
    )
    sd.wait()

    # Save to temporary WAV file
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
        wav.write(tmp.name, sample_rate, recording)
        audio_path = tmp.name

    print("📝 Transcribing...")

    # Send to Groq Whisper
    with open(audio_path, "rb") as f:
        transcript = client.audio.transcriptions.create(
            model="whisper-large-v3",
            file=(audio_path, f.read()),
        )

    text = transcript.text.strip()
    print(f"📢 You said: {text}")

    return text