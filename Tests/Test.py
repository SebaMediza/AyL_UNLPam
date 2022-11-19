import xml.etree.ElementTree as ET


def parse(file):
    with open(file, 'r') as anfd:
        test = ET.parse(anfd)
        root = test.getroot()
        for y in root:
            for g in y.findall('state'):
                if g.find('initial') is None and g.find('final') is not None:
                    print(g.attrib)


if __name__ == '__main__':
    archivo = '../TP_4/AFND_epsilon.jff'
    parse(archivo)
