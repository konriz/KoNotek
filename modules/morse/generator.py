import numpy as np
import struct

sampling_rate = 44100
frequency = 440
sample = 1000000
x = np.arange(sample)

y = 100*np.sin(2 * np.pi * frequency * x / sampling_rate)

with open('test.wav', 'wb') as file:
    for i in y:
        print(i)
        file.write(struct.pack('b', int(i)))

print(len(y))

