# DECODING MORSE CODE PROGRAM

# Morse Code Dictionary
MORSE_CODE = {".-": "A",
            "-...": "B",
            "-.-.": "C",
            "-..": "D",
            ".": "E",
            "..-.": "F",
            "--.": "G",
            "....": "H",
            "..": "I",
            ".---": "J",
            "-.-": "K",
            ".-..": "L",
            "--": "M",
            "-.": "N",
            "---": "O",
            ".--.": "P",
            "--.-": "Q",
            ".-.": "R",
            "...": "S",
            "-": "T",
            "..-": "U",
            "...-": "V",
            ".--": "W",
            "-..-": "X",
            "-.--": "Y",
            "--..": "Z",
            "-----": "0",
            ".----": "1",
            "..---": "2",
            "...--": "3",
            "....-": "4",
            ".....": "5",
            "-....": "6",
            "--...": "7",
            "---..": "8",
            "----.": "9",
            "--..--": ",",
            ".-.-.-": ".",
            "..--..": "?",
            "-.-.--": "!",
            "---...": ":",
            "...---...": "SOS"}


def decodeMorse(morse_code):
    list_of_words_in_morse_code = morse_code.split("   ")
    decode_morse_code = []
    
    for n, word in enumerate(list_of_words_in_morse_code):
        list_of_char = word.split(" ")
        word_decoded = []
        for char in list_of_char:
            word_decoded.append(MORSE_CODE.get(char, char))
        decode_morse_code.append("".join(word_decoded))
        decode_morse_code[n].replace(' ','')
    
    decode_morse_code = list(filter(None, decode_morse_code))
    decode_morse_code = " ".join(decode_morse_code)
    return decode_morse_code


# Testing function
if __name__ == "__main__":
    message = "...---...  -.-.--    ...---...  -.-.--    ...---...  -.-.--  -.-.--  -.-.--"
    print(decodeMorse(message))