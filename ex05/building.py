import string
import sys


def count_characters(text: str) -> None:
    """Count and display the different character types in a string."""
    upper = sum(1 for char in text if char.isupper())
    lower = sum(1 for char in text if char.islower())
    punctuation = sum(1 for char in text if char in string.punctuation)
    spaces = sum(1 for char in text if char.isspace())
    digits = sum(1 for char in text if char.isdigit())

    print(f"The text contains {len(text)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main() -> None:
    """Read the input and count its characters."""
    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")

        if len(sys.argv) == 2 and sys.argv[1] != "":
            text = sys.argv[1]
        else:
            print("What is the text to count?", end="", flush=True)
            text = sys.stdin.read()

        count_characters(text)

    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
