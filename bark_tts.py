
import numpy as np
from scipy.io.wavfile import write

def generate_audio(text, output_path):
    print(f"Generating audio for: {text}")
    sample_rate = 24000
    duration = 5  # seconds
    frequency = 440  # Hz
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    tone = 0.5 * np.sin(2 * np.pi * frequency * t)
    write(output_path, sample_rate, tone.astype(np.float32))

if __name__ == "__main__":
    generate_audio("A beautiful sunset over the ocean.", "output/voice.wav")
