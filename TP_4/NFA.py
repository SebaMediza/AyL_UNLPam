import xml.etree.ElementTree as ET


class NFA(object):
    initial = ''
    final = ''
    cadena = ''
    read = ''
    to = ''
    fromm = ''
    actual = ''

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
                    elif x.find('final') is not None:
                        self.final = x.get('id')
                        print('Estado final: ', self.final)

    def run(self, word):
        print('Cadena a reconocer: ', word)
        self.cadena = word
        self.parse('./AFND.jff')

    def parse(self, filename):
        with open(filename, 'r') as anfd:
            test = ET.parse(anfd)
            root = test.getroot()
            while self.cadena != '':
                for y in root:
                    for x in y.findall('transition'):
                        self.read = x.find('read').text
                        self.fromm = x.find('from').text
                        if self.cadena[0] == self.read and self.actual == self.fromm:
                            self.cadena = self.cadena[1:]
                            self.actual = x.find('to').text
            return self.actual == self.final


if __name__ == '__main__':
    p = NFA('./AFND.jff')
    p.run('abbbaa')
