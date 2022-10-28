import xml.etree.ElementTree as ET


def turing_machine(cadena: str, regla: str):
    with open(regla, 'r') as file:
        turing = ET.parse(file)
        myroot = turing.getroot()
        i = 0
        estado_actual = '0'
        for y in myroot:
            for t in y.findall('block'):
                final = t.find('final')
                if final is not None:
                    print(cadena, t.get('id'))

            for x in y.findall('transition'):
                fromm = x.find('from').text
                to = x.find('to').text
                if fromm == estado_actual:
                    read = x.find('read').text
                    write = x.find('write').text
                    if cadena[i] == read:
                        cadena = write + cadena[1:]
                        estado_actual = to
                        i = i + 1
                    elif cadena[i] == '#':
                        print(cadena[0:(len(cadena)-1)])
                        return True


if __name__ == '__main__':
    string = '1#'
    reglas = r'C:\Users\sebam\Documents\Programacion\AyL_UNLPam\TP_2\EJ_3.jff'
    print(turing_machine(string, reglas))
