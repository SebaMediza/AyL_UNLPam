import json


def turing_machine(cadena: str, regla: str) -> bool:
    with open(regla, 'r') as turing:
        data = json.load(turing)
        q = data['Q']
        delta = data['Delta']
        first = data['q0']
        end = data['F']
        now = first
        while now != end:
            for i in cadena:
                if i in first:
                    print(i)
                now = delta['q1']
                if i in now:
                    print(i)
                if i == '#':
                    now = end

    return True


if __name__ == '__main__':
    string = '00001111#'
    reglas = r'C:\Users\sebam\Documents\Programacion\AyL_UNLPam\TP_2\data.json'
    print(turing_machine(string, reglas))
