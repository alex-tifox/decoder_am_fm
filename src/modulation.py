import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

from signal_analysis import spectrum


def low_pass_filter(cutoff, time):
    f = np.sin(0.3 * cutoff * time) / (np.pi * time)
    return f


def am_modulation(carrier_freq, modulator_signal, modulator_samplerate):
    time = np.linspace(0, len(modulator_signal) / modulator_samplerate, len(modulator_signal))
    carrier_signal = 1 * np.cos(2 * np.pi * time * carrier_freq)
    modulated_signal = modulator_signal * carrier_signal

    return modulated_signal


def fm_modulation():
    pass


def am_demodulation(modulated_signal, carrier_freq, samplerate, message_freq):
    time = np.linspace(0, len(modulated_signal) / samplerate, len(modulated_signal))
    carrier_signal = 1 * np.cos(2 * carrier_freq * time)

    filtered = iir_bp_filter(modulated_signal, 7200, 19000, 100000)
    # filtered =
    # filtered = modulated_signal
    spectrum(filtered, samplerate)
    plt.show()
    plt.title("Spectrum of filtered")

    demodulated = filtered * carrier_signal
    return demodulated


def fm_demodulation():
    pass


def generate_wave(amplitude, freq, time):
    return amplitude * np.sin(2 * np.pi * time * freq)


def iir_bp_filter(source, left_lim, right_lim, samplerate):
    sos = signal.iirfilter(17, [left_lim, right_lim], rs=50, btype='band', analog=False, ftype='cheby2', fs=samplerate, output='sos')

    w, h = signal.sosfreqz(sos, samplerate, fs=samplerate)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.semilogx(w, 20 * np.log10(np.maximum(abs(h), 1e-5)))
    ax.set_title('Characteristics IIR bandpass')
    ax.set_xlabel('Frequency [Hz]')
    ax.set_ylabel('Amplitude [dB]')
    ax.axis((10, 1000, -100, 10))
    ax.grid(which='both', axis='both')
    plt.show()

    return signal.sosfilt(sos, source)


def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = signal.butter(order, normal_cutoff, btype='low', analog=False)
    return b, a


def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = signal.lfilter(b, a, data)
    return y
