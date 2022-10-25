import xml.etree.ElementTree as ET


class ParseA(object):

    def __init__(self):
        self.cadena = None

    def evaluate(self, cadena):
        self.cadena = cadena
        self.S()

    def S(self):
        print(self.cadena)


if __name__ == '__main__':
    p = ParseA
    chain = '(a+a)$'
    print(p.evaluate(chain))
