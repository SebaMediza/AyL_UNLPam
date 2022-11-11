"""
    Ejercicio 1: Para cada una de las siguientes gramáticas hacer:
        • Determinar si es LL1 construyendo la tabla correspondiente.
        • Para las que no sean LL1 intentar hacer alguna modificación a la gramática (por
          ejemplo, factorizar o eliminar recursividad izquierda), de tal modo que se
          conviertan en otras gramáticas que lo sean.
        • Dado una cadena cualquiera realizar el árbol de análisis sintáctico.

    b) S → aAS | b      Es LL1
       A → a | bSA
"""


class ParserB(object):

    def __init__(self):  # Constructor que inicializa la cadena con None
        self.cadena = None

    def evaluate(self, cadena):  # Metodo principal de del parsing, recibe por parametro, la cadena a analizar
        self.cadena = cadena
        self.S()
        return self.cadena[0] == '$'

    """
        Funcionamiento basico, cada metodo de la clase, lee el primer terminal de la cadena
        y segun la tabla LL1, hace la llamada a otro metodo o llama al metodo match()
    """

    # Por cada NO terminal se implemeto un metodo
    def S(self):
        if self.cadena[0] == 'a':
            self.match('a')
            self.A()
            self.S()
        elif self.cadena[0] == 'b':
            self.match('b')
        elif self.cadena == '$':
            raise Exception('Error')

    def A(self):
        if self.cadena[0] == 'a':
            self.match('a')

        elif self.cadena[0] == 'b':
            self.match('b')
            self.S()
            self.A()

    """
            Este metodo recibe por parametro un simbolo terminal y se encarga, en caso de que el terminal pertenezca al
            lenguaje, de sacar el terminal pasado por parametro de la cadena
        """

    def match(self, s):
        if s == self.cadena[0]:
            self.cadena = self.cadena[1:]
        else:
            raise Exception("Error", "En Match")

        """
           En todos los metodos en caso de que el terminal no pertenezca al lenugaje
           dispara una excepcion la cual indica que la cadena no pertenece a ese lenguaje
        """


if __name__ == '__main__':
    p = ParserB()
    word = 'abba'
    print(p.evaluate(word + '$'))
