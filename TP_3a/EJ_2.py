import xml.etree.ElementTree as ET
file = r'C:\Users\sebam\Documents\Programacion\AyL_UNLPam\TP_3a\1a.jff'
with open(file, 'r') as rules:
    ll1 = ET.parse(rules)
    myroot = ll1.getroot()

    def macht(string: str, stack: str):
        while string[0] == stack[0]:
            string = string[1:]
            stack = stack[1:]
        if stack[0] == 'S':
            S(stack)

    def S(string: str):
        for x in myroot.findall('production'):
            right = x.find('right').text
            left = x.find('left').text
            if string[0] == right[0]:
                pila = right
                macht(string, pila)
            if string[0] == left[0]:
                macht(string, pila)

    def F(string: str):
        pila = string
        S(pila)

if __name__ == '__main__':
    chain = '(a+a)$'
    S(chain)