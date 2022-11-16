import xml.etree.ElementTree as ET


class NFA(object):
    initial = ''
    final = ''
    cadena = ''
    read = ''
    fromm = ''
    actual = ''
    lenguaje = []
    newStates = []
    AFND = False
    result = None
    archivo = ''

    def __init__(self, file=None):
        super(NFA, self).__init__()
        self.load_from_file(file)

    def load_from_file(self, filename):
        self.archivo = filename

    def run(self, word):
        with open(self.archivo, 'r') as anfd:
            test = ET.parse(anfd)
            root = test.getroot()
            for y in root:
                for x in y.findall('state'):
                    if x.find('initial') is not None:
                        self.initial = x.get('id')
                        self.actual = self.initial
                        print('Estado inicial:', self.initial)
                    if x.find('final') is not None:
                        self.final = x.get('id')
                        print('Estado final:', self.final)
                for t in y.findall('transition'):
                    if t.find('read').text not in self.lenguaje:
                        self.lenguaje.append(t.find('read').text)
                for g in y.findall('transition'):
                    if g.find('read').text is None:
                        self.AFND = True
        print('El lenguaje reconocido es:', self.lenguaje)
        print('Cadena a reconocer:', word)
        self.cadena = word
        if self.AFND is False:
            self.parse(self.archivo)
        else:
            self.split(self.archivo)
        return self.result

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
            self.result = self.actual == self.final

    def split(self, filename):
        with open(filename, 'r') as AFND:
            machine = ET.parse(AFND)
            root = machine.getroot()
            for y in root:
                for x in y.findall('transition'):
                    if x.find('read').text is None:
                        self.newStates.append(x.find('to').text)
                        self.add(filename)
                        break
        self.splitParse(filename)

    def add(self, filename):
        with open(filename, 'r') as AFND:
            machine = ET.parse(AFND)
            root = machine.getroot()
            for y in root:
                for x in y.findall('transition'):
                    if self.newStates[0] == x.find('from').text:
                        self.newStates.append(x.find('to').text)

    def splitParse(self, filename):
        with open(filename, 'r') as AFND:
            machine = ET.parse(AFND)
            root = machine.getroot()
            while self.cadena != '':
                for y in root:
                    for x in y.findall('transition'):
                        self.read = x.find('read').text
                        self.fromm = x.find('from').text
                        if self.cadena[0] == self.read and self.fromm in self.newStates and self.actual == self.fromm:
                            self.cadena = self.cadena[1:]
                            self.actual = x.find('to').text
                            break
            self.result = self.actual == self.final


if __name__ == '__main__':
    p = NFA('./AFND_epsilon.jff')
    print('Resultado:', p.run('1111'))
