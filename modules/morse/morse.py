
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
    ' ': '//',
    '.': '///'
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
        if letter != ' ' and letter != '.':
            morse.append(SIGN_TO_MORSE[''])
    return ''.join(morse)


def convert_morse_to_string(message):
    string = []
    signs = message.split('/')
    for letter in signs:
        if letter == '/' or letter == '':
            letter = ''.join([letter, '//'])
        string.append(MORSE_TO_SIGN[letter])
    return ''.join(string)


test = convert_string_to_morse('Hello world.')
print(test)
retest = convert_morse_to_string(test)
print(retest)
