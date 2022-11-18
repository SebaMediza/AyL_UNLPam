# from itertools import chain, combinations
#
#
# # Mejor opción:
# def powerset(iterable):
#     s = list(iterable)
#     return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))
#
#
# def main():
#     l1 = ["p", "q", "r", "s"]
#
#     print([i for i in powerset(l1)], "\n")
#

def modulo(num):
    for numm in num:
        if (numm % 3) == 0:
            print(numm, 'Es Modulo de Tres')
        else:
            print(numm, 'No es Modulo de Tres')


if __name__ == '__main__':
    index = [
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19
    ]
    modulo(index)
