import xml.dom.minidom


def turing_machine(cadena: str, regla: str) -> None:
    rules = xml.dom.minidom.parse(regla)
    bloques = rules.getElementsByTagName('transition')
    transicionFrom = rules.getElementsByTagName('from')
    transicionTo = rules.getElementsByTagName('to')
    readCharacter = rules.getElementsByTagName('read')
    writeCharacter = rules.getElementsByTagName('write')
    movement = rules.getElementsByTagName('move')
    final = rules.getElementByTagName('final')
    # print("%d block" % bloques.length)
    print(transicionTo)
    print(transicionFrom)
    # while transicionTo != final:



if __name__ == '__main__':
    string = '0'
    reglas = r'C:\Users\sebam\Documents\Programacion\AyL_UNLPam\TP_2\EJ_1.jff'
    turing_machine(string, reglas)
