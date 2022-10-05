import xml.dom.minidom


def turing_machine(cadena: str, regla: str) -> None:
    rules = xml.dom.minidom.parse(regla)
    bloques = rules.getElementsByTagName('transition')
    transicionFrom = rules.getElementsByTagName('from')
    transicionTo = rules.getElementsByTagName('to')
    readCharacter = rules.getElementsByTagName('read')
    writeCharacter = rules.getElementsByTagName('write')
    movement = rules.getElementsByTagName('move')
    # print("%d block" % bloques.length)
    while transicionTo != 4:
        for i in cadena:
            print(cadena.index(i))


if __name__ == '__main__':
    string = '0010010101010'
    reglas = r'C:\Users\sebam\Documents\Programacion\AyL_UNLPam\TP_2\EJ_1.jff'
    turing_machine(string, reglas)
