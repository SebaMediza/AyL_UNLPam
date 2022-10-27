import xml.etree.ElementTree as ET


def turing_machine(cadena: str, regla: str):
    with open(regla, 'r') as file:
        turing = ET.parse(file)
        myroot = turing.getroot()
        for y in myroot:
            for x in y.findall('transition'):
                desde = x.find('from').text
                to = x.find('to').text
                read = x.find('read').text
                write = x.find('write').text
                move = x.find('move').text
                print(desde, to, read, write, move)


if __name__ == '__main__':
    string = '00001111#'
    reglas = r'C:\Users\sebam\Documents\Programacion\AyL_UNLPam\TP_2\EJ_3.jff'
    turing_machine(string, reglas)
