import numpy as np
import matplotlib.pyplot as plt

import file_manipulation
from signal_analysis import spectrum


def get_white_noise():
    noise_data, samplerate = file_manipulation.read_wav_from_file(filename='noises/white.wav')

    return noise_data


def add_noise_to_signal(signal, samplerate):
    alpha_coeff = 0.5
    noise = get_white_noise()

    noised_signal = np.copy(signal)

    for i in range(len(signal)):
        noised_signal[i] = signal[i] * alpha_coeff + (noise[i % samplerate] * (1-alpha_coeff))

    spectrum(noised_signal, samplerate)
    plt.show()

    return noised_signal
