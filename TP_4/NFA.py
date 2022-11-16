import xml.etree.ElementTree as ET


class NFA(object):
    initial = ''
    final = ''
    cadena = ''
    read = ''
    fromm = ''
    actual = ''
    lenguaje = []

    def __init__(self, file=None):
        super(NFA, self).__init__()
        self.load_from_file(file)

    def load_from_file(self, filename):
        with open(filename, 'r') as anfd:
            test = ET.parse(anfd)
            root = test.getroot()
            for y in root:
                for x in y.findall('state'):
                    if x.find('initial') is not None:
                        self.initial = x.get('id')
                        self.actual = self.initial
                        print('Estado inicial: ', self.initial)
                    if x.find('final') is not None:
                        self.final = x.get('id')
                        print('Estado final: ', self.final)
                for t in y.findall('transition'):
                    if t.find('read').text not in self.lenguaje:
                        self.lenguaje.append(t.find('read').text)
        print('El lenguaje reconocido es: ', self.lenguaje)

    def run(self, word):
        print('Cadena a reconocer: ', word)
        self.cadena = word
        # print(self.parse('./AFND_epsilon.jff'))

    def parse(self, filename):
        with open(filename, 'r') as anfd:
            test = ET.parse(anfd)
            root = test.getroot()
            while self.cadena != '':
                for y in root:
                    for x in y.findall('transition'):
                        if self.cadena != '':
                            self.read = x.find('read').text
                            self.fromm = x.find('from').text
                            if self.cadena[0] == self.read and self.actual == self.fromm:
                                self.cadena = self.cadena[1:]
                                self.actual = x.find('to').text
                            elif self.read is None and self.actual == self.fromm:
                                self.actual = x.find('to').text
            return self.actual == self.final


if __name__ == '__main__':
    p = NFA('./AFND_epsilon.jff')
    p.run('0011')
