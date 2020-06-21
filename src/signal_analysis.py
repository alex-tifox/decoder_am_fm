import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


def data_for_spectrum(data, fs):
    fft_res = np.fft.fft(data)
    wave_freqs = np.fft.fftfreq(len(fft_res)) * fs

    return fft_res, wave_freqs


def spectrum(data, samplerate):
    fft_res, wave_freqs = data_for_spectrum(data, samplerate)

    plt.subplot(1, 2, 1)
    plt.plot(wave_freqs[:int(len(wave_freqs) / 2)], 20 * np.log10(fft_res)[:int(len(fft_res) / 2)])
    plt.ylabel("Power [dB]")
    plt.xlabel("Frequency [Hz]")
    plt.title("Signal spectrum")

    plt.subplot(1, 2, 2)
    plt.plot(data)
    plt.ylabel("Amplitude")
    plt.xlabel("Time [s]")
    plt.title("Signal")


def spectrogram(yaxis):
    my = np.array(yaxis)
    f, t, Sxx = signal.spectrogram(my, 44100)
    plt.pcolormesh(t, f, Sxx)
    plt.xlabel('Time [Sec]')
    plt.ylabel('Frequency [Hz]')
    plt.title('Signal spectrogram')
    plt.show()

    return f, t, Sxx


def display_signal(data, samplerate):
    plt.plot(np.linspace(0, len(data) / samplerate, len(data)), data)
    plt.ylabel("Amplitude")
    plt.xlabel("Time [s]")
    plt.title("Signal")