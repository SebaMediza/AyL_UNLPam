class ParserC(object):
    def __init__(self):
        self.cadena = None

    def evaluate(self, cadena):
        self.cadena = cadena
        self.S()
        return self.cadena[0] == '$'

    def S(self):
        if self.cadena[0] == 'a':
            self.match('a')
            self.T()
        elif self.cadena[0] == 'b':
            pass

    def T(self):
        if self.cadena[0] == 'a':
            self.match('a')
            self.S()
            self.match('b')
            self.match('b')
        elif self.cadena[0] == 'b':
            pass

    def match(self, s):
        if s == self.cadena[0]:
            self.cadena = self.cadena[1:]
        else:
            raise Exception("Error", "En Match")


if __name__ == '__main__':
    p = ParserC()
    word = 'aaaaaabbbbb'
    print(p.evaluate(word + '$'))
