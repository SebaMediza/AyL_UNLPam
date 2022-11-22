import xml.etree.ElementTree as ET


class NFA(object):
    initial = ''
    final = ''
    cadena = ''
    read = ''
    fromm = ''
    actual = ''
    lenguaje = []
    newstates = []
    finalstates = []
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
            self.split()
        return self.result

    def parse(self):
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
                    while self.cadena != '':
                        for x in y.findall('transition'):
                            if self.cadena != '':
                                self.read = x.find('read').text
                                self.fromm = x.find('from').text
                                if self.cadena[0] == self.read and self.actual == self.fromm:
                                    self.cadena = self.cadena[1:]
                                    self.actual = x.find('to').text
                    self.result = self.actual == self.final

    def split(self):
        if len(self.newstates) == 0:
            with open(self.archivo, 'r') as anfd:
                test = ET.parse(anfd)
                root = test.getroot()
                for y in root:
                    for x in y.findall('state'):
                        if x.find('initial') is not None:
                            self.newstates.append(x.get('id'))
                            self.splitparse()
        else:
            self.newstates.clear()
            with open(self.archivo, 'r') as anfd:
                test = ET.parse(anfd)
                root = test.getroot()
                for y in root:
                    for x in y.findall('transition'):
                        if x.find('read').text is None:
                            self.newstates.append(x.find('to').text)
                            for t in y.findall('transition'):
                                if t.find('from').text in self.newstates:
                                    self.newstates.append(t.find('to').text)
                            self.splitparse()

    def splitparse(self):
        with open(self.archivo, 'r') as anfd:
            test = ET.parse(anfd)
            root = test.getroot()
            for y in root:
                for x in y.findall('state'):
                    if x.find('initial') is not None:
                        self.initial = x.get('id')
                        self.actual = self.initial
                    if x.find('final') is not None and x.get('id') not in self.finalstates:
                        self.finalstates.append(x.get('id'))
                for t in y.findall('transition'):
                    if t.find('read').text not in self.lenguaje:
                        self.lenguaje.append(t.find('read').text)
            while self.actual != self.fromm or self.cadena != '':
                for y in root:
                    for x in y.findall('state'):
                        if x.find('initial') is None and x.find('final') is None and x.get('id') in self.newstates:
                            self.actual = x.get('id')
                            break
                        elif x.find('initial') is not None and x.get('id') in self.newstates:
                            self.actual = x.get('id')
                        elif x.find('final') is not None and x.get('id') in self.newstates:
                            self.actual = x.get('id')
                            break
                    for x in y.findall('transition'):
                        if self.cadena != '':
                            self.read = x.find('read').text
                            self.fromm = x.find('from').text
                            if self.cadena[0] == self.read and self.actual == self.fromm and self.fromm in self.newstates:
                                self.cadena = self.cadena[1:]
                                self.actual = x.find('to').text
                                self.newstates.clear()
                        else:
                            self.result = self.actual in self.finalstates
                            return self.result
                self.split()
