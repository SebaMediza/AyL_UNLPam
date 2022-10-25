import xml.etree.ElementTree as ET


def parseA(table: str, cadena: str):

    def macht(string: str, stack: str):
        while string[0] == stack[0]:
            string = string[1:]
            stack = stack[1:]
            if string[0] == '$':
                print('La cadena pertenece al lenguaje')
                exit(0)
            else:
                print('La cadena NO pertenece al Lenguaje')
                exit(1)
        if stack[0] == 'S':
            S(string, stack)
        if stack[0] == 'A':
            A(string, stack)

    def S(string: str, stack: str):
        for x in myroot.findall('production'):
            right = x.find('right').text
            left = x.find('left').text
            if stack[0] == left[0] and string[0] == right[0]:
                stack = right
                break
            if stack[0] == 'S' and string[0] == 'a':
                stack = 'F' + stack[1:]
                break
        macht(string, stack)

    def A(string: str, stack: str):
        for x in myroot.findall('production'):
            right = x.find('right').text
            left = x.find('left').text
            if stack[0] == left[0] and string[0] == right[0]:
                stack = 'a' + stack[1:]
                break
        macht(string, stack)

    with open(table, 'r') as rules:
        ll1 = ET.parse(rules)
        myroot = ll1.getroot()
        pila = 'S'
        S(cadena, pila)


if __name__ == '__main__':
    file = r'C:\Users\sebam\Documents\Programacion\AyL_UNLPam\TP_3a\1b.jff'
    chain = 'aab$'
    print(parseA(file, chain))
