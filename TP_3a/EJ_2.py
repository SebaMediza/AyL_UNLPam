class Parser(object):
    """
    Parser LL1
        Gramática original:
            S -> 0S1
            S -> 01

        Gramática LL1:
            S -> 0T
            T -> S1
            T -> 1
    """

    def __init__(self):
        self.cadena = None

    def evaluate(self, cadena):
        """
        Evalúa la cadena
        :param cadena:
        :return True | False:
        """
        self.cadena = cadena
        self.S()
        return self.cadena[0] == "$"

    def S(self):
        print("S", self.cadena)
        if self.cadena[0] == "a":
            self.match("a")
            # self.F()
        else:
            raise Exception("Error", "En S")

    def F(self):
        print("T", self.cadena)
        if self.cadena[0] == "0":
            self.S()
            self.match("1")
        elif self.cadena[0] == "1":
            self.match("1")
        else:
            raise Exception("Error", "En T")

    def match(self, s):
        print("M", self.cadena, s)
        if s == self.cadena[0]:
            self.cadena = self.cadena[1:]
        else:
            raise Exception("Error", "En Match")


if __name__ == '__main__':
    p = Parser()
    print(p.evaluate('a$'))
