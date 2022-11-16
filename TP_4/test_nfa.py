import unittest
from TP_4.NFA import NFA


class TestCaseNFA1(unittest.TestCase):
    """
    NFA-ε, with a binary alphabet, that determines if the input contains an even number of 0s or an even number of 1s.
                                 λ
                      ┌───────────────┐
                      ▼               │
    0   ┌────┐      ┌──────┐   0    ┌───────┐
  ┌──── │    │      │      │ ────┐  │       │
  │     │ q4 │  1   │ * q3 │     │  │ -> q0 │
  └───▶ │    │ ◀─── │      │ ◀───┘  │       │
        └────┘      └──────┘        └───────┘
          │    1      ▲               │
          └───────────┘               │ λ
                                      ▼
                                1   ┌───────┐
                              ┌──── │       │
                              │     │ * q1  │
                              └───▶ │       │ ◀┐
                                    └───────┘  │
                                      │        │
                                      │ 0      │ 0
                                      ▼        │
                                1   ┌───────┐  │
                              ┌──── │       │  │
                              │     │  q2   │  │
                              └───▶ │       │ ─┘
                                    └───────┘
    """
    def test(self):
        v = [
            ("", True),
            ("11100", True),
            ("10001", True),
            ("0001111", True),
            ("01111", True),
            ("11111", True),
            ("1", True),
            ("101010", False),
            ("111101", False),
            ("10000001", True),
            ("01111110", True),
            ("01110110", False),
            ("100011110", True),
            ("011100001", True),
            ("0", True),
            ("000001", False),
            ("111110", False)
        ]
        p = NFA("AFND_epsilon_even_0_or_1.jff")
        for t in v:
            with self.subTest(t[0]):
                r = p.run(t[0])
                self.assertEqual(r, t[1])


class TestCaseNFA2(unittest.TestCase):
    """
    NFA for grammar:
        S	-->	0S | 1A
        A	--> 1A | empty

┌───────┐
│ -> q0 │ ────┐ 0
│       │ ◀───┘
└───────┘
  │ λ
  ▼
┌───────┐   1
│  q1   │ ────┐
│       │ ◀───┘
└───────┘
  │ 1
  ▼
┌───────┐
│ * q2  │
└───────┘
    """
    def test(self):
        v = [
            ("", False),
            ("0", False),
            ("1", True),
            ("0000", False),
            ("1111", True),
            ("0011", True),
            ("01", True),
            ("010", False),
            ("101", False)
        ]
        p = NFA("AFND_epsilon.jff")
        for t in v:
            with self.subTest(t[0]):
                r = p.run(t[0])
                self.assertEqual(r, t[1])


class TestCaseFA(unittest.TestCase):
    """
    Deterministic finite automaton that accepts only binary words whit even number of 0's && even number of 1's
          0
  ┌───────────────┐
  │               │
  │               │
  │    ┌──────────┼───────────────┐
  │    │          ▼               │
  │    │        ┌────────┐        │
  │    │    ┌─▶ │ ->* q0 │ ─┐     │
  │    │    │   └────────┘  │     │
  │    │    │     │         │     │ 0
  │    │    │ 1   │ 1       │     │
  │    │    │     ▼         │     │
  │    │    │   ┌────────┐  │     │
  │    │    └── │   q1   │ ◀┼─────┘
  │    │        └────────┘  │
  │    │          │         │
  │    │          │ 0       │
  │    │          ▼         │
  │    │        ┌────────┐  │
  │    └─────── │   q3   │ ◀┼─────┐
  │             └────────┘  │     │
  │               │         │     │
  │               │ 1       │ 0   │
  │               ▼         │     │
  │             ┌────────┐  │     │ 1
  └──────────── │   q2   │ ◀┘     │
                └────────┘        │
                  │               │
                  └───────────────┘
    """
    def test(self):
        v = [
            ("1", False),
            ("0", False),
            ("10", False),
            ("01", False),
            ("11", True),
            ("00", True),
            ("100", False),
            ("101", False),
            ("1001", True),
            ("1010", True),
            ("0101", True),
            ("10000000000111", True),
            ("01111111111000", True)
        ]
        p = NFA("AFD_even_0_and_1.jff")
        for t in v:
            with self.subTest(t[0]):
                r = p.run(t[0])
                self.assertEqual(r, t[1])


class TestCaseFA_M3(unittest.TestCase):
    """
    Deterministic finite automaton that accepts only binary numbers that are multiples of 3
    0   ┌────────┐
  ┌──── │        │
  │     │ ->* q0 │
  └───▶ │        │ ◀┐
        └────────┘  │
          │         │
          │ 1       │ 1
          ▼         │
        ┌────────┐  │
  ┌───▶ │   q1   │ ─┘
  │     └────────┘
  │       │
  │ 0     │ 0
  │       ▼
  │     ┌────────┐   1
  │     │        │ ────┐
  │     │   q2   │     │
  └──── │        │ ◀───┘
        └────────┘
    """
    def test(self):
        v = [
            ("0", True),
            ("1", False),
            ("10", False),
            ("11", True),
            ("100", False),
            ("101", False),
            ("110", True),
            ("111", False),
            ("1000", False),
            ("1001", True),
            ("1010", False),
            ("1011", False),
            ("1100", True),
            ("1101", False),
            ("1110", False),
            ("1111", True)
        ]
        p = NFA("AFD_multiples_of_3.jff")
        for t in v:
            with self.subTest(t[0]):
                r = p.run(t[0])
                self.assertEqual(r, t[1])


if __name__ == '__main__':

    unittest.main()
    unittest.result
