import xml.etree.ElementTree as ET


class NFA(object):
    initial = ''
    final = ''
    cadena = ''
    read = ''
    fromm = ''
    actual = ''
    lenguaje = []
    newstates = [
        ['0'],
        ['1', '2']
    ]
    # newstates = [
    #     ['0'],
    #     ['1', '2'],
    #     ['3', '4']
    # ]
    AFND = False
    result = None
    archivo = ''

    def __init__(self, file=None):
        super(NFA, self).__init__()
        self.load_from_file(file)

    def load_from_file(self, filename):
        self.archivo = filename

    def run(self, word):
        self.cadena = word
        with open(self.archivo, 'r') as anfd:
            test = ET.parse(anfd)
            root = test.getroot()
            for y in root:
                for g in y.findall('transition'):
                    if g.find('read').text is None:
                        self.AFND = True
        if self.AFND is False:
            self.parse()
        else:
            self.splitparse()
        return self.result

    def parse(self):
        with open(self.archivo, 'r') as anfd:
            test = ET.parse(anfd)
            root = test.getroot()
            while self.cadena != '':
                for y in root:
                    for x in y.findall('state'):
                        if x.find('initial') is not None:
                            self.initial = x.get('id')
                            self.actual = self.initial
                        if x.find('final') is not None:
                            self.final = x.get('id')
                    for t in y.findall('transition'):
                        if t.find('read').text not in self.lenguaje:
                            self.lenguaje.append(t.find('read').text)
                    for x in y.findall('transition'):
                        if self.cadena != '':
                            self.read = x.find('read').text
                            self.fromm = x.find('from').text
                            if self.cadena[0] == self.read and self.actual == self.fromm:
                                self.cadena = self.cadena[1:]
                                self.actual = x.find('to').text
            self.result = self.actual == self.final

    def splitparse(self):
        with open(self.archivo, 'r') as anfd:
            test = ET.parse(anfd)
            root = test.getroot()
            for y in root:
                for x in y.findall('state'):
                    if x.find('initial') is not None:
                        self.initial = x.get('id')
                        self.actual = self.initial
                    if x.find('final') is not None:
                        self.final = x.get('id')
                for t in y.findall('transition'):
                    if t.find('read').text not in self.lenguaje:
                        self.lenguaje.append(t.find('read').text)
            while self.actual != self.fromm or self.cadena != '':
                for lista in self.newstates:
                    for y in root:
                        for x in y.findall('transition'):
                            if self.cadena != '':
                                self.read = x.find('read').text
                                self.fromm = x.find('from').text
                                if self.cadena[0] == self.read and self.actual == self.fromm and self.fromm in lista:
                                    self.cadena = self.cadena[1:]
                                    self.actual = x.find('to').text
                                elif self.read is None:
                                    self.actual = x.find('to').text
                            else:
                                self.result = self.actual == self.final
                                return self.result


if __name__ == '__main__':
    p = NFA('./AFND_epsilon.jff')
    print('Resultado:', p.run('101'))
