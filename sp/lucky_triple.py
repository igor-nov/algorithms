"""
A “lucky triple” is a tuple (x, y, z) where y divides by x and z divides by y, such as [1, 2, 4].

Write a function that takes a list of positive integers l and counts the number of “lucky triples” of (lx, ly, lz) where
 the list indices meet the requirement x <= y <= z. The length of l is between 2 and 2000 inclusive. The elements are
 between 1 and 999,999 inclusive. Some lists does not contain any “lucky triples” and in that case return 0.

Given, A = [1, 2, 3, 4, 5, 6], the answer is 3.
Given, A = [1, 1, 1], the answer is 1.
Given, A = [1, 2, 4, 16], the answer is 4
Given, A = [3, 7, 13], the answer is 0
"""


def lucky_triple(inp):
    res, inp_len, couples = 0, len(inp), set()

    for ind_lo in range(inp_len):
        for ind_hi in range(ind_lo + 1, inp_len):
            # print(f'{ind_lo}|{ind_hi}, {inp[ind_hi]} % {inp[ind_lo]}')
            if not inp[ind_hi] % inp[ind_lo]:
                couples.add((ind_lo, ind_hi))

    #print(couples)
    for couple in couples:
        _, ind_lo = couple  # swap lo with hi to start from last found element
        for ind_hi in range(ind_lo + 1, inp_len):
            if not inp[ind_hi] % inp[ind_lo]:
                res += 1

    return res



# get_primes(1, 10)

#############
import unittest


class TestCase(unittest.TestCase):

    def test1(self):
        inp = [1, 2, 3, 4, 5, 6]
        out = 3
        res = lucky_triple(inp)
        self.assertEqual(res, out)

    def test2(self):
        inp = [1, 1, 1]
        out = 1
        res = lucky_triple(inp)
        self.assertEqual(res, out)

    def test3(self):
        inp = [1, 2, 4, 16]
        out = 4
        res = lucky_triple(inp)
        self.assertEqual(res, out)

    def test4(self):
        inp = [3, 7, 13]
        out = 0
        res = lucky_triple(inp)
        self.assertEqual(res, out)

    def test5(self):
        inp = [1, 2, 4]
        out = 1
        res = lucky_triple(inp)
        self.assertEqual(res, out)

    def test6(self):
        inp = [1, 2, 4, 8]
        out = 4
        res = lucky_triple(inp)
        self.assertEqual(res, out)

    def test7(self):
        inp = [1, 2, 3, 4, 5, 6, 8, 9]
        out = 7
        res = lucky_triple(inp)
        self.assertEqual(res, out)

    def test6(self):
        inp = [1, 8, 2, 4]
        out = 1
        res = lucky_triple(inp)
        self.assertEqual(res, out)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
