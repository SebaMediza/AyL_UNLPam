import xml.etree.ElementTree as ET


def parse_a(table: str, string: str):
    print(string)
    with open(table, 'r') as rules:
        ll1 = ET.parse(rules)
        myroot = ll1.getroot()
        for x in myroot.findall('production'):
            right = x.find('right').text
            if string[0] == right[0]:
                print('Elemento del XML: ', right[0])
                print('Elemmento de la Cadena: ', string[0])
                string = string[1:]
                print(string)
                print(True)


if __name__ == '__main__':
    file = r'C:\Users\sebam\Documents\Programacion\AyL_UNLPam\TP_3a\1a.jff'
    cadena = '(a+a)$'
    parse_a(file, cadena)
