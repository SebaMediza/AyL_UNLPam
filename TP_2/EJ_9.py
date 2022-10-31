import xml.etree.ElementTree as ET


def turing_machine(cadena: str, regla: str):
    with open(regla, 'r') as file:
        turing = ET.parse(file)
        myroot = turing.getroot()
        estadoActual = '0'
        for y in myroot:
            for t in y.findall('block'):
                if t.find('final') is not None:
                    final = t.get('id')

            for x in y.findall('transition'):
                read = x.find('read').text
                write = x.find('write').text
                if cadena[0] == read and estadoActual == '0':
                    estadoActual = x.find('from').text
                    proximoEstado = x.find('to').text
                    cadena = write + cadena[1:]
                    proximoEstado = estadoActual
                    if proximoEstado == final:
                        exit(0)


if __name__ == '__main__':
    string = '00001111#'
    reglas = r'C:\Users\sebam\Documents\Programacion\AyL_UNLPam\TP_2\EJ_1.jff'
    turing_machine(string, reglas)
