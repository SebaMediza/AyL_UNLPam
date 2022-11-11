"""
    Ejercicio 1: Para cada una de las siguientes gramáticas hacer:
        • Determinar si es LL1 construyendo la tabla correspondiente.
        • Para las que no sean LL1 intentar hacer alguna modificación a la gramática (por
          ejemplo, factorizar o eliminar recursividad izquierda), de tal modo que se
          conviertan en otras gramáticas que lo sean.
        • Dado una cadena cualquiera realizar el árbol de análisis sintáctico.

    c) S → aaSbb | a | ε        NO en LL1

        S → aT | ε
        T → aSbb | ε
"""


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
