"""
script.py

Example script that uses signals.py:
- Generate sine and unit step signals
- Apply time shift and time scaling
- Save plots in 'plots/' folder
"""

import os
from signals import generate_sine, generate_unit_step, time_shift, time_scale, plot_signal


def main():
    # Create folder for plots
    if not os.path.exists("plots"):
        os.makedirs("plots")

    fs = 1000       # Sampling frequency in Hz
    duration = 1.0  # Signal duration in seconds

    # 1) Generate a sine wave
    t, sine = generate_sine(frequency=5, amplitude=1, phase=0, duration=duration, fs=fs)
    plot_signal(t, {"sine": sine}, "Sine wave", "plots/sine.png")

    # 2) Generate a unit step
    t_u, u = generate_unit_step(duration=duration, fs=fs, step_time=0.2)
    plot_signal(t_u, {"unit step": u}, "Unit step", "plots/unit_step.png")

    # 3) Apply time shift to sine wave
    t_shift, sine_shift = time_shift(t, sine, shift=0.1, fs=fs)
    plot_signal(t, {"sine": sine, "sine shifted": sine_shift}, "Time shift", "plots/sine_shift.png")

    # 4) Apply time scaling to sine wave
    t_scale, sine_scaled = time_scale(t, sine, scale=2.0)
    plot_signal(t, {"sine": sine, "sine scaled": sine_scaled}, "Time scaling", "plots/sine_scaled.png")

    print("Plots saved in 'plots/' folder.")


if __name__ == "__main__":
    main()
