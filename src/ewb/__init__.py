# Copyright (c) 2014 James Utter, All rights reserved.
#
# @author: see AUTHORS file

__all__ = ["blink", "position", "radio", "texttospeech"]

from ewb.position import GPS as gps

from ewb.fm_radio import get_radio as radio

# the following dictionary is derived from the morse package for python
# @author: Augie Fackler <durin42@gmail.com>
morse_code = {
        '!': '-.-.--',
        "'": '.----.',
        '"': '.-..-.',
        '$': '...-..-',
        '&': '.-...',
        '(': '-.--.',
        ')': '-.--.-',
        '+': '.-.-.',
        ',': '--..--',
        '-': '-....-',
        '.': '.-.-.-',
        '/': '-..-.',
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
        ':': '---...',
        ';': '-.-.-.',
        '=': '-...-',
        '?': '..--..',
        '@': '.--.-.',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '_': '..--.-',
        ' ': ' ',
        }
