import xml.etree.ElementTree as ET


class ParserA(object):
    def parseA(self: str, cadena: str):
        def macht(string: str, stack: str, resultado: str):
            while string[0] == stack[0]:
                string = string[1:]
                stack = stack[1:]
                if string[0] == '$':
                    print('La cadena pertenece al lenguaje')
                    exit(0)
            if stack[0] == 'S':
                S(string, stack, resultado)
            if stack[0] == 'A':
                A(string, stack, resultado)

        def S(string: str, stack: str, resultado: str):
            for x in myroot.findall('production'):
                right = x.find('right').text
                left = x.find('left').text
                if stack[0] == left[0] and string[0] == right[0]:
                    stack = right + stack[1:]
                    break
                if stack[0] == 'S' and string[0] == 'a':
                    stack = 'F' + stack[1:]
                    break
            macht(string, stack, resultado)
            return resultado

        def A(string: str, stack: str, resultado: str):
            for x in myroot.findall('production'):
                right = x.find('right').text
                left = x.find('left').text
                if stack[0] == left[0] and string[0] == right[0]:
                    stack = right + stack[1:]
                    break
            macht(string, stack, resultado)
            return resultado

        with open(self, 'r') as rules:
            ll1 = ET.parse(rules)
            myroot = ll1.getroot()
            pila = 'S'
            result = ''
            result = S(cadena, pila, result)
            return result


if __name__ == '__main__':
    file = r'C:\Users\sebam\Documents\Programacion\AyL_UNLPam\TP_3a\1b.jff'
    chain = 'abbaabbaabbaabbab'
    p = ParserA

    print(chain, p.parseA(file, chain + '$'))
