import json


def testuringmachine(cadena: str, turing_machine: str) -> bool:
    json.load(cadena, turing_machine)
    return False


if __name__ == '__main__':
    string = '00010010101010'
    testuringmachine(string)
