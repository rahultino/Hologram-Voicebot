import sounddevice as sd
import numpy as np

print("Testing microphone... speak for 3 seconds.")

duration = 3
sample_rate = 16000

rec = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
sd.wait()

print("Recording shape:", rec.shape)
print("If no errors, mic works.")
