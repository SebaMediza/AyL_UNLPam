import json


def turing_machine(cadena: str, regla: str) -> bool:
    json.load(regla)


if __name__ == '__main__':
    string = '00010010101010'
    reglas = r'C:\Users\sebam\Documents\Programacion\AyL_UNLPam\TP_2\data.json'
    turing_machine(string, reglas)
