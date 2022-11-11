class parser(object):
    def __init__(self):
        self.cadena = None

    def evaluate(self, cadena):
        self.cadena = cadena
        self.S()
        return self.cadena[0] == '$'

    def S(self):
        if self.cadena[0] == '0':
            self.match('0')
            self.T()
        elif self.cadena[0] == '1':
            self.match('1')
            self.T()
        elif self.cadena[0] == '2':
            self.match('2')
            self.T()
        elif self.cadena[0] == '3':
            self.match('3')
            self.T()
        elif self.cadena[0] == '4':
            self.match('4')
            self.T()
        elif self.cadena[0] == '5':
            self.match('5')
            self.T()
        elif self.cadena[0] == '6':
            self.match('6')
            self.T()
        elif self.cadena[0] == '7':
            self.match('7')
            self.T()
        elif self.cadena[0] == '8':
            self.match('8')
            self.T()
        elif self.cadena[0] == '9':
            self.match('9')
            self.T()
        elif self.cadena[0] == '$':
            pass

    def T(self):
        if self.cadena[0] == '0':
            self.match('0')
            self.S()
        elif self.cadena[0] == '1':
            self.match('1')
            self.S()
        elif self.cadena[0] == '2':
            self.match('2')
            self.S()
        elif self.cadena[0] == '3':
            self.match('3')
            self.S()
        elif self.cadena[0] == '4':
            self.match('4')
            self.S()
        elif self.cadena[0] == '5':
            self.match('5')
            self.S()
        elif self.cadena[0] == '6':
            self.match('6')
            self.S()
        elif self.cadena[0] == '7':
            self.match('7')
            self.S()
        elif self.cadena[0] == '8':
            self.match('8')
            self.S()
        elif self.cadena[0] == '9':
            self.match('9')
            self.S()
        elif self.cadena[0] == '$':
            pass

    def match(self, s):
        if s == self.cadena[0]:
            self.cadena = self.cadena[1:]
        else:
            raise Exception("Error", "En Match")


if __name__ == '__main__':
    p = parser()
    word = '1298756621596'
    print(p.evaluate(word + '$'))
