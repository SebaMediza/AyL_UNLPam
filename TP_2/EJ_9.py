import xml.etree.ElementTree as ET


def turing_machine(cadena: str, regla: str):
    with open(regla, 'r') as file:
        turing = ET.parse(file)
        myroot = turing.getroot()
        index = 0
        for y in myroot:
            for h in y.findall('block'):
                if h.find('initial') is not None:
                    inicial = h.get('id')
            for t in y.findall('block'):
                if t.find('final') is not None:
                    final = t.get('id')
        while cadena[index] != '#':
            for x in y.findall('transition'):
                read = x.find('read').text
                write = x.find('write').text
                estadoActual = x.find('from').text
                if cadena[index] == read and estadoActual == inicial:
                    cadena = write + cadena[1:]
                    proximoEstado = x.find('to').text
                    inicial = proximoEstado
                    index = index + 1


if __name__ == '__main__':
    string = '1 '
    reglas = r'C:\Users\sebam\Documents\Programacion\AyL_UNLPam\TP_2\EJ_3.jff'
    turing_machine(string, reglas)
