import file_manipulation


def get_white_noise():
    noise_data, samplerate = file_manipulation.read_wav_from_file(filename='noises/white.wav')

    return noise_data
