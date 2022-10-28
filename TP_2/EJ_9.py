import xml.etree.ElementTree as ET


def turing_machine(cadena: str, regla: str):
    with open(regla, 'r') as file:
        turing = ET.parse(file)
        myroot = turing.getroot()
        for y in myroot:
            for t in y.findall('block'):
                final = t.find('final')
                if final is not None:
                    print(cadena, t.get('id'))

            for x in y.findall('transition'):
                fromm = x.find('from').text
                to = x.find('to').text
                read = x.find('read').text
                write = x.find('write').text

                if cadena[0] == read:
                    cadena = write + cadena[1:]
                    to = fromm
                    if to == t.get('id'):
                        exit(0)


if __name__ == '__main__':
    string = '00001111#'
    reglas = r'C:\Users\sebam\Documents\Programacion\AyL_UNLPam\TP_2\EJ_1.jff'
    turing_machine(string, reglas)
