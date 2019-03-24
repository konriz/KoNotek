import numpy as np
import struct


class Signal:

    def __init__(self, type, length):
        self.type = type
        self.length = length


SIGNAL_RULES = {
    ".": Signal(type='signal', length=1),
    "-": Signal(type='signal', length=3),
    "/": Signal(type='pause', length=2),
    "*": Signal(type='pause', length=6)
}


class Writer:

    def __init__(self, file_name, freq=440, short_length=0.1, sampling_rate=44100):
        self.file_name = file_name
        self.freq = freq
        self.short_length = short_length
        self.sampling_rate = sampling_rate

        self.sample = self.sampling_rate / self.freq
        self.repetitions = short_length * freq

    def __generate_wave(self, length=1):

        x = np.arange(self.sample * self.repetitions * length)
        y = 100 * np.sin(2 * np.pi * self.freq * x / self.sampling_rate)
        return y

    def __generate_pause(self, length=1):

        x = np.arange(self.sample * self.repetitions * length)
        y = 0 * x
        return y

    def __write_signal(self, signal):
        with open(self.file_name, 'ab') as file:
            for sample in signal:
                file.write(struct.pack('b', int(sample)))

    def __write(self, sign):
        signal = SIGNAL_RULES[sign]
        print('Writing ' + sign)
        if signal.type == 'pause':
            self.__write_signal(self.__generate_pause(signal.length))
        else:
            self.__write_signal(self.__generate_wave(signal.length))
            self.__write_signal(self.__generate_pause())

    def write_morse_wav(self, morse):
        for sign in morse:
            self.__write(sign)
