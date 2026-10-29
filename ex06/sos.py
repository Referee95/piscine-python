import sys


NESTED_MORSE = {
    " ": "/",
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
}


def encode_morse(text: str) -> str:
    """Convert a string into Morse code."""
    return " ".join(NESTED_MORSE[char.upper()] for char in text)


def main() -> None:
    """Validate the argument and display its Morse encoding."""
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")

        text = sys.argv[1]

        if any(char.upper() not in NESTED_MORSE for char in text):
            raise AssertionError("the arguments are bad")

        print(encode_morse(text))

    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
