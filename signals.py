"""
signals.py

Basic functions to generate and manipulate signals.
Includes:
- sine wave
- unit step
- time shift
- time scaling
"""

import numpy as np
import matplotlib.pyplot as plt


def generate_sine(frequency, amplitude, phase, duration, fs):
    """
    Generate a sampled sine wave.

    Parameters
    ----------
    frequency : float
        Frequency in Hz.
    amplitude : float
        Amplitude of the sine wave.
    phase : float
        Phase in radians.
    duration : float
        Duration of the signal in seconds.
    fs : float
        Sampling frequency in Hz.

    Returns
    -------
    t : np.ndarray
        Time vector.
    x : np.ndarray
        Sine wave values.
    """
    t = np.arange(0, duration, 1 / fs)
    x = amplitude * np.sin(2 * np.pi * frequency * t + phase)
    return t, x


def generate_unit_step(duration, fs, step_time=0.0):
    """
    Generate a unit step signal u(t - step_time).

    Parameters
    ----------
    duration : float
        Duration of the signal in seconds.
    fs : float
        Sampling frequency in Hz.
    step_time : float
        Time where the step begins.

    Returns
    -------
    t : np.ndarray
        Time vector.
    u : np.ndarray
        Step signal values (0 or 1).
    """
    t = np.arange(0, duration, 1 / fs)
    u = np.where(t >= step_time, 1, 0)
    return t, u


def time_shift(t, x, shift, fs):
    """
    Apply time shifting: y(t) = x(t - shift).

    Parameters
    ----------
    t : np.ndarray
        Original time vector.
    x : np.ndarray
        Original signal.
    shift : float
        Time shift in seconds (positive means delay).
    fs : float
        Sampling frequency in Hz.

    Returns
    -------
    t : np.ndarray
        Same time vector.
    y : np.ndarray
        Shifted signal.
    """
    sample_shift = int(shift * fs)
    if sample_shift > 0:
        y = np.concatenate((np.zeros(sample_shift), x[:-sample_shift]))
    elif sample_shift < 0:
        y = np.concatenate((x[-sample_shift:], np.zeros(-sample_shift)))
    else:
        y = x.copy()
    return t, y


def time_scale(t, x, scale):
    """
    Apply time scaling: y(t) = x(scale * t).

    Parameters
    ----------
    t : np.ndarray
        Original time vector.
    x : np.ndarray
        Original signal.
    scale : float
        Time scale factor (>1 compresses, <1 stretches).

    Returns
    -------
    t : np.ndarray
        Same time vector.
    y : np.ndarray
        Scaled signal.
    """
    new_t = scale * t
    y = np.interp(t, new_t, x, left=0, right=0)
    return t, y


def plot_signal(t, signals, title, filename):
    """
    Plot signals and save the figure.

    Parameters
    ----------
    t : np.ndarray
        Time vector.
    signals : dict
        Dictionary {label: signal}.
    title : str
        Plot title.
    filename : str
        File path to save the figure.
    """
    for label, sig in signals.items():
        plt.plot(t, sig, label=label)
    plt.title(title)
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.legend()
    plt.savefig(filename, dpi=150)
    plt.close()
