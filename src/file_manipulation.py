import soundfile


def read_wav_from_file(filename='dtmf_from_string.wav'):
    wav_data, samplerate = soundfile.read(filename)

    return wav_data, samplerate
