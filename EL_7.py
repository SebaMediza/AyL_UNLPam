import re


def convert(input_file_path: str, output_fil_path: str) -> None:
    # rmd=Read_MOCK_DATA // wmd=Write_MOCK_DATA
    re_str = r'(\d+),(\w+\W*\w+),(\w+\W?\s?\w+\s?\w+\W*\w*\W*?),(\w+)(\@\w*\W?\w+\.?\w+\.?\w+),(\w+),(.*)'
    re_str_mod = r'\1,\3,\2,\4@ing.unlpam.edu.ar,\7'
    with open(input_file_path, 'r', encoding="UTF-8") as rmd:
        with open(output_fil_path, 'w', encoding="UTF-8") as wmd:
            for line in rmd:
                line = re.sub(re_str, re_str_mod, line)
                wmd.write(line)


if __name__ == '__main__':
    Input = r"C:\Users\arcen\Documents\AyL\AyL_UNLPam\MOCK_DATA.csv"
    Output = r"C:\Users\arcen\Documents\AyL\AyL_UNLPam\MOCK_DATA_MOD.csv"
    convert(Input, Output)
