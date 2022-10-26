class ParserA(object):

    def __init__(self):
        self.cadena = None

    def evaluate(self, cadena):
        self.cadena = cadena
        self.S()
        return self.cadena[0] == '$'

    def S(self):
        if self.cadena[0] == '(':
            self.match('(')
            self.F()
        elif self.cadena[0] == 'a':
            self.match('a')

    def F(self):
        if self.cadena[0] == 'a':
            self.match('a')
            self.F()
        elif self.cadena[0] == '+':
            self.match('+')
            self.F()
        elif self.cadena[0] == ')':
            self.match(')')
            self.F()
        elif self.cadena[0] == '(':
            self.match('(')
            self.S()

    def match(self, s):
        if s == self.cadena[0]:
            self.cadena = self.cadena[1:]
        else:
            raise Exception("Error", "En Match")


if __name__ == '__main__':
    p = ParserA()
    word = '(((((a+a)+a)+a)+a)+a)'
    print(p.evaluate(word + '$'))
