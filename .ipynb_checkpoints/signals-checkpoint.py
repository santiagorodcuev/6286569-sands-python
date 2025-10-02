import numpy as np
import matplotlib.pyplot as plt

def create_sine_wave(frequency, duration):
    t = np.linspace(0, duration, int(44100 * duration))
    y = np.sin(2 * np.pi * frequency * t)
    return t, y

t, y = create_sine_wave(1, 2)
plt.plot(t, y)
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.title("Sine Wave")
plt.show()