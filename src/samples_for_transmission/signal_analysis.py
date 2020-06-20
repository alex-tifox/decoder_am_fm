import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

import noises


def data_for_spectrum(data, fs):
    fft_res = np.fft.fft(data)
    wave_freqs = np.fft.fftfreq(len(fft_res)) * fs

    return fft_res, wave_freqs


def spectrum(data, fs):
    fft_res, wave_freqs = data_for_spectrum(data, fs)

    plt.plot(wave_freqs[:int(len(wave_freqs) / 2)], 20 * np.log10(fft_res)[:int(len(fft_res) / 2)])
    plt.xlabel("Frequency [Hz]")
    plt.ylabel("Power [dB]")
    plt.title("Widmo sygnału")


def spectrogram(yaxis):
    my = np.array(yaxis)
    f, t, Sxx = signal.spectrogram(my, 44100)
    plt.pcolormesh(t, f, Sxx)
    plt.xlabel('Time [Sec]')
    plt.ylabel('Frequency [Hz]')
    plt.title('Spektrogram sygnału')
    plt.show()

    return f, t, Sxx


def add_noise_to_signal(signal, samplerate, alpha_coeff):
    noise_name = "white"
    noise = noises.get_white_noise()
    if noise_name == "white":
        noise = noises.get_white_noise()

    noised_signal = np.copy(signal)

    for i in range(len(signal)):
        noised_signal[i] = signal[i] * alpha_coeff + (noise[i % samplerate] * (1-alpha_coeff))

    plt.figure()
    plt.subplot(1, 2, 1)
    plt.plot(noised_signal)
    plt.ylabel("Amplitude")
    plt.xlabel("Time (number of probes)")
    plt.title("Signal + {} noise".format(noise_name))
    plt.subplot(1, 2, 2)

    spectrum(noised_signal, samplerate)
    plt.show()

    return noised_signal
