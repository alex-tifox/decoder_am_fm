import signal_analysis
import file_manipulation as f_man
import matplotlib.pyplot as plt


data, samplerate = f_man.read_wav_from_file('./samples_for_transmission/radio_1.wav')

signal_analysis.spectrum(data, samplerate)
plt.show()
signal_analysis.spectrogram(data)
