import xml.etree.ElementTree as ET


class ParseC(object):
    def evaluate(self, cadena: str):

        def macht(string: str, stack: str):
            while string[0] == stack[0]:
                stack = stack[1:]
                string = string[1:]
                if string[0] == '$':
                    print('La cadena pertenece al Legunaje')
                    exit(0)
            if stack[0] == 'S':
                S(string, stack)
            if stack[0] == 'T':
                T(string, stack)

        def S(string: str, stack: str):
            for x in myroot.findall('production'):
                right = x.find('right').text
                left = x.find('left').text
                if stack[0] == 'S' and right is None:
                    stack = stack[1:]
                    break
                if stack[0] == left[0] and string[0] == right[0]:
                    stack = right + stack[1:]
                    break
            macht(string, stack)

        def T(string: str, stack: str):
            for x in myroot.findall('production'):
                right = x.find('right').text
                left = x.find('left').text
                if stack[0] == left[0] and string[0] == right[0]:
                    stack = right + stack[1:]
                    break
            macht(string, stack)

        with open(self, 'r') as rules:
            ll1 = ET.parse(rules)
            myroot = ll1.getroot()
            pila = 'S'
            S(cadena, pila)


if __name__ == '__main__':
    file = r'C:\Users\sebam\Documents\Programacion\AyL_UNLPam\TP_3a\1c.jff'
    chain = 'aabb$'
    p = ParseC
    print(p.evaluate(file, chain))
