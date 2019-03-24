from modules.morse.generator import Writer

SIGN_TO_MORSE = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '': '/',
    ' ': '*',
    ',': '--..--',
    '.': '.-.-.-'
}


def invert_dict(dictionary):
    inverted_dict = {}
    for word in dictionary:
        inverted_dict[dictionary[word]] = word
    return inverted_dict


MORSE_TO_SIGN = invert_dict(SIGN_TO_MORSE)


def convert_string_to_morse(message):
    morse = []
    for letter in message.lower():
        morse.append(SIGN_TO_MORSE[letter])
        if letter != '.':
            morse.append(SIGN_TO_MORSE[''])
    return ''.join(morse)


def convert_morse_to_string(message):
    string = []
    signs = message.split('/')
    for letter in signs:
        if letter == '':
            letter = ''.join([letter, '/'])
        string.append(MORSE_TO_SIGN[letter])
    return ''.join(string)


def translate(mode, input):
    output = ''
    try:
        if mode == 'to_code':
            output = convert_string_to_morse(input)
        elif mode == 'to_letters':
            output = convert_morse_to_string(input)
        else:
            raise Exception("Wrong mode")
    except KeyError as e:
        output = "Sign {e} not valid".format(e=e)
    return output


def convert_morse_to_audio(message):
    writer = Writer(file_name="Hello.wav")
    writer.write_morse_wav(message)
