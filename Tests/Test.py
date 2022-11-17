from itertools import chain, combinations


# Mejor opción:
def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def main():
    l1 = ["p", "q", "r", "s"]

    print([i for i in powerset(l1)], "\n")


if __name__ == '__main__':
    main()
