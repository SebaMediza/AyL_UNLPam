import unittest

from TP_3a.parse_a import ParserA
from TP_3a.parse_b import ParserB
from TP_3a.parse_c import ParserC
from TP_3a.parse_d import ParserD


class TestCaseParse(unittest.TestCase):
    def test_a(self):
        v = [
            ("a", True),
            ("aa", False),
            ("(a+a)", True),
            ("(((((a+a)+a)+a)+a)+a)", True)
        ]
        p = ParserA()
        for t in v:
            with self.subTest(t[0]):
                r = p.evaluate(t[0] + "$")
                self.assertEqual(r, t[1])

    def test_a_exception(self):
        v = [("(a+(a+a))"), ("")]
        p = ParserA()
        for t in v:
            with self.subTest(t):
                self.assertRaises(Exception, p.evaluate, t + "$")

    def test_b(self):
        v = [
            ("aab", True),
            ("aaaab", True),
            ("aaba", False),
            ("abbab", True),
            ("abbaaab", True),
            ("aaaaaaaab", True),
            ("abbaabbaabbaabbab", True)
        ]

        p = ParserB()
        for t in v:
            with self.subTest(t[0]):
                r = p.evaluate(t[0] + "$")
                self.assertEqual(r, t[1])

    def test_b_exception(self):
        p = ParserB()
        self.assertRaises(Exception, p.evaluate, "abba")

    def test_c(self):
        v = [
            ("a", True),
            ("aabb", True),
            ("aaabb", True),
            ("aaaaabbbb", True),
            ("aaaaaabbbbbb", True),
            ("b", False)
        ]
        p = ParserC()
        for t in v:
            with self.subTest(t[0]):
                r = p.evaluate(t[0] + "$")
                self.assertEqual(r, t[1])

    def test_c_exception(self):
        v = ["aaaaaabbbbb", "aaaaababbbbb", "aaaaaaaaaaaaab"]
        p = ParserC()
        for t in v:
            with self.subTest(t):
                self.assertRaises(Exception, p.evaluate, t + "$")

    def test_d(self):
        v = [
            ("a", True),
            ("aa", True),
            ("aaa", True),
            ("aaaa", True),
            ("b", True),
            ("bb", True),
            ("bbb", True),
            ("bbbb", True),
            ("", True)
        ]
        p = ParserD()
        for t in v:
            with self.subTest(t[0]):
                r = p.evaluate(t[0] + "$")
                self.assertEqual(r, t[1])

    def test_d_exception(self):
        v = ["aaaab", "bbbba"]
        p = ParserD()
        for t in v:
            with self.subTest(t):
                self.assertRaises(Exception, p.evaluate, t + "$")


if __name__ == '__main__':
    unittest.main()