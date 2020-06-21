import signal_analysis
import file_manipulation as f_man
import modulation

import matplotlib.pyplot as plt

data, samplerate = f_man.read_wav_from_file('./samples_for_transmission/radio_1.wav')

# samplerate = 1000
# data = modulation.generate_wave(2, 5, np.linspace(0, 2, 2 * samplerate))

signal_analysis.display_signal(data, samplerate)
plt.show()

data = modulation.am_modulation(carrier_freq=500000, modulator_signal=data, modulator_samplerate=samplerate)
samplerate = 1000000
signal_analysis.spectrum(data, samplerate)
plt.show()
signal_analysis.spectrogram(data)

demod = modulation.am_demodulation(data, 500000, 1000000, 15000)

signal_analysis.spectrum(demod, 44100)
plt.title("Spectrum of demodulated")
plt.show()

f_man.write_result_to_file('demoded_res.wav', demod)
