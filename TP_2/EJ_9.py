import xml.etree.ElementTree as ET


def turing_machine(cadena: str, regla: str):
    with open(regla, 'r') as file:
        turing = ET.parse(file)
        myroot = turing.getroot()
        result = ''
        indice = 0
        lenguaje = []
        for y in myroot:
            for h in y.findall('block'):
                if h.find('initial') is not None:
                    inicial = h.get('id')
                    estadoActual = inicial
            for t in y.findall('block'):
                if t.find('final') is not None:
                    final = t.get('id')
            for t in y.findall('transition'):
                index = 0
                lenguaje.insert(index, t.find('write').text)
        while estadoActual != final:
            for x in y.findall('transition'):
                read = x.find('read').text
                write = x.find('write').text
                fromm = x.find('from').text
                direction = x.find('move').text
                if cadena == '':
                    cadena = None
                if cadena is None and read is None:
                    estadoActual = x.find('to').text
                if cadena is not None:
                    if cadena[0] not in lenguaje:
                        return 'La cadena no pertenece al leguaje reconocido por la maquina', False
                    if cadena[0] == read and estadoActual == fromm and direction == 'R':
                        cadena = cadena[1:]
                        result = result[0:indice] + write + result[indice + 1:]
                        indice = indice + 1
                        estadoActual = x.find('to').text
                        break
                    if cadena[0] == read and estadoActual == fromm and direction == 'L':
                        cadena = cadena[1:]
                        result = result[indice + 1:] + write + result[0:indice]
                        indice = indice + 1
                        estadoActual = x.find('to').text
                        break
        return estadoActual == final, result


if __name__ == '__main__':
    string = '0110'
    reglas = r'C:\Users\sebam\Documents\Programacion\AyL_UNLPam\TP_2\EJ_5.jff'
    print('Cadena: ', string)
    print('Cadena devuelta por la maquina: ', turing_machine(string, reglas))
