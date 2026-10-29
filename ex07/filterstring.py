import sys


def filter_words(text: str, number: int) -> list[str]:
    """Return words longer than the given number of characters."""
    words = text.split()
    return [word for word in words if (lambda w: len(w) > number)(word)]


def main() -> None:
    """Validate arguments and display the filtered words."""
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")

        text = sys.argv[1]
        number = int(sys.argv[2])

        if text.isdigit() or not text:
            raise AssertionError("the arguments are bad")

        result = filter_words(text, number)
        print(result)

    except (AssertionError, ValueError):
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
