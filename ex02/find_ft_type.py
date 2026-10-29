from typing import Any


def all_thing_is_obj(object: Any) -> int:
    if isinstance(object, list):
        print("List :")
    elif isinstance(object, tuple):
        print("Tuple :")
    elif isinstance(object, set):
        print("Set :")
    elif isinstance(object, dict):
        print("Dict :")
    elif isinstance(object, str):
        if object == "Brian":
            print("Brian is in the kitchen :")
        elif object == "Toto":
            print("Toto is in the kitchen :")
        else:
            print("Type not found")
    else:
        print("Type not found")

    return 42