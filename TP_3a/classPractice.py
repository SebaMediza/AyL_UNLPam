import xml.etree.ElementTree as ET


class ParserA(object):

    def __init__(self):
        self.string = None
        self.stack = None
        self.file = None
        self.myroot = None

    def evaluate(self, cadena, file):
        self.string = cadena
        self.file = file
        with open(self.file, 'r') as rules:
            ll1 = ET.parse(rules)
            self.myroot = ll1.getroot()
            self.stack = 'S'
            self.S(self.myroot)
            return self.string[0] == '$'

    def macht(self):
        while self.string[0] == self.stack[0]:
            self.string = self.string[1:]
            self.stack = self.stack[1:]
        if self.stack[0] == 'S':
            self.S(self.myroot)
        if self.stack[0] == 'F':
            self.F(self.myroot)

    def S(self, myroot):
        for x in myroot.findall('production'):
            right = x.find('right').text
            left = x.find('left').text
            if self.stack[0] == left[0] and self.string[0] == right[0]:
                self.stack = right + self.stack[1:]
                break
            if self.stack[0] == 'S' and self.string[0] == 'a':
                self.stack = 'F' + self.stack[1:]
                break
        self.macht()

    def F(self, myroot):
        for x in myroot.findall('production'):
            right = x.find('right').text
            left = x.find('left').text
            if self.stack[0] == left[0] and self.string[0] == right[0]:
                self.stack = 'a' + self.stack[1:]
                break
        self.macht()


if __name__ == '__main__':
    p = ParserA()
    word = '(a+a)'
    table = r'C:\Users\sebam\Documents\Programacion\AyL_UNLPam\TP_3a\1a.jff'
    self = ''
    print(p.evaluate(word + '$', table))
