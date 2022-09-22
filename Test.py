if __name__ == '__main__':
    with open('MOCK_DATA.csv', 'r', encoding="Latin-1") as my_list:
        for line in my_list:
            print(line, end="")
