import xml.etree.ElementTree as ET


class ParserC(object):
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
        if self.string[0] == '$':
            return True

    def macht(self):
        while self.string[0] == self.stack[0]:
            self.string = self.string[1:]
            self.stack = self.stack[1:]
        if self.stack[0] == 'S':
            self.S(self.myroot)
        if self.stack[0] == 'T':
            self.T(self.myroot)

    def S(self, myroot):
        for x in myroot.findall('production'):
            right = x.find('right').text
            left = x.find('left').text
            if self.stack[0] == 'S' and right is None:
                self.stack = self.stack[1:]
                break
            if self.stack[0] == left[0] and self.string[0] == right[0]:
                self.stack = right + self.stack[1:]
                break
        self.macht()

    def T(self, myroot):
        for x in myroot.findall('production'):
            right = x.find('right').text
            left = x.find('left').text
            if self.stack[0] == left[0] and self.string[0] == right[0]:
                self.stack = right + self.stack[1:]
                break
        self.macht()


if __name__ == '__main__':
    p = ParserC()
    word = 'aabb'
    table = r'C:\Users\sebam\Documents\Programacion\AyL_UNLPam\TP_3a\parser_c_tabla_ll1.jff'
    print(p.evaluate(word + '$', table))
