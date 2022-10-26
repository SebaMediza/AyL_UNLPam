class ParserD(object):
    def __init__(self):
        self.cadena = None

    def evaluate(self, cadena):
        self.cadena = cadena
        self.S()
        return self.cadena[0] == '$'

    def S(self):
        if self.cadena[0] == 'a':
            self.F()
        elif self.cadena[0] == 'b':
            self.F()
        elif self.cadena[0] == '$':
            pass

    def F(self):
        if self.cadena[0] == 'a':
            self.match('a')
            self.S()
        elif self.cadena[0] == 'b':
            self.match('b')
            self.S()

    def match(self, s):
        if s == self.cadena[0]:
            self.cadena = self.cadena[1:]
        else:
            raise Exception("Error", "En Match")
