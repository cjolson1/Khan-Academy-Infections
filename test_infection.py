from user import *
from limited_infection import limited_infection
from total_infection import total_infection
import unittest
from sys import maxint


class InfectionTests(unittest.TestCase):
    def testOne(self):
        """
        Test #1: Simple Link Total Infection.
        """
        a = User('a')
        b = User('b')
        coach(a, b)
        total_infection(a, 1)
        self.failUnless(a.get_version() == 1 and b.get_version() == 1)

    def testTwo(self):
        """
        Test #2: Tree Total Infection from top node.
        """
        a = User('a')
        b = User('b')
        c = User('c')
        d = User('d')
        e = User('e')
        f = User('f')
        g = User('g')
        coach(a, b)
        coach(a, c)
        coach(b, d)
        coach(b, e)
        coach(c, f)
        coach(c, g)
        users = [a, b, c, d, e, f, g]
        total_infection(a, 1)
        correct = True
        for user in users:
            if user.get_version() != 1:
                correct = False
        self.failUnless(correct)

    def testThree(self):
        """
        Test #3: Tree Total Infection from leaf.
        """
        a = User('a')
        b = User('b')
        c = User('c')
        d = User('d')
        e = User('e')
        f = User('f')
        g = User('g')
        coach(a, b)
        coach(a, c)
        coach(b, d)
        coach(b, e)
        coach(c, f)
        coach(c, g)
        users = [a, b, c, d, e, f, g]
        total_infection(g, 1)
        correct = True
        for user in users:
            if user.get_version() != 1:
                correct = False
        self.failUnless(correct)

    def testFour(self):
        """
        Test #4: Complex Multiple Graph Total Infection.
        """
        a = User('a')
        b = User('b')
        c = User('c')
        d = User('d')
        e = User('e')
        f = User('f')
        g = User('g')
        h = User('h')
        i = User('i')
        j = User('j')
        coach(a, b)
        coach(a, c)
        coach(b, a)
        coach(d, c)
        coach(c, b)
        coach(e, f)
        coach(g, b)
        coach(b, d)
        coach(c, h)
        coach(h, i)
        coach(b, j)
        coach(d, j)
        total_infection(a, 1)
        correct = True
        for user in [a,b,c,d,g,h,i,j]:
            if user.get_version() != 1:
                correct = False
        self.failUnless(correct)

    def testFive(self):
        """
        Test #5: Simple Link Child Limited Infection.
        """
        a = User('a')
        b = User('b')
        c = User('c')
        d = User('d')
        coach(a, b)
        coach(b, c)
        coach(c, d)
        users = [a, b, c]
        limited_infection([a, b, c, d], a, 1, 'child', 3)
        correct = True
        for user in users:
            if user.get_version() != 1:
                correct = False
        self.failUnless(correct)

    def testSix(self):
        """
        Test #6: Simple Link Parent Limited Infection.
        """
        a = User('a')
        b = User('b')
        c = User('c')
        d = User('d')
        coach(a, b)
        coach(b, c)
        coach(c, d)
        users = [d, c]
        limited_infection([a, b, c, d], d, 1, 'parent', 2)
        correct = True
        for user in users:
            if user.get_version() != 1:
                correct = False
        self.failUnless(correct)

    def testSeven(self):
        """
        Test #7: Tree Child Limited Infection from top node.
        """
        a = User('a')
        b = User('b')
        c = User('c')
        d = User('d')
        e = User('e')
        f = User('f')
        g = User('g')
        coach(a, b)
        coach(a, c)
        coach(b, d)
        coach(b, e)
        coach(c, f)
        coach(c, g)
        users = [a, b, c, d, e, f, g]
        limited_infection([a, b, c, d, e, f, g], a, 1, 'child', 5)
        count = 0
        for user in users:
            if user.get_version() == 1:
                count += 1
        self.failUnless(
                        count == 5 and
                        e.get_version() == 1 == d.get_version() and f.get_version() is g.get_version() is None or
                        f.get_version() == 1 == g.get_version() and e.get_version() is g.get_version() is None
                        )

    def testEight(self):
        """
        Test #8: Tree Parent Limited Infection from leaf.
        """
        a = User('a')
        b = User('b')
        c = User('c')
        d = User('d')
        e = User('e')
        f = User('f')
        g = User('g')
        coach(a, b)
        coach(a, c)
        coach(b, d)
        coach(b, e)
        coach(c, f)
        coach(c, g)
        users = [a, b, c, d, e, f, g]
        limited_infection([a, b, c, d, e, f, g], f, 1, 'parent', maxint)
        count = 0
        for user in users:
            if user.get_version() == 1:
                count += 1
        self.failUnless(
                        count == 3 and
                        f.get_version() == 1 == c.get_version() == a.get_version()
                        )

    def testNine(self):
        """
        Test #9: Tree Child Limited Infection from middle.
        """
        a = User('a')
        b = User('b')
        c = User('c')
        d = User('d')
        e = User('e')
        f = User('f')
        g = User('g')
        coach(a, b)
        coach(a, c)
        coach(b, d)
        coach(b, e)
        coach(c, f)
        coach(c, g)
        users = [a, b, c, d, e, f, g]
        limited_infection(users, c, 1, 'child', maxint)
        self.failUnless(
                        c.get_version() == 1 == f.get_version() == g.get_version()
                        )

    def testTen(self):
        """
        Test #10: Tree Parent Limited Infection from middle.
        """
        a = User('a')
        b = User('b')
        c = User('c')
        d = User('d')
        e = User('e')
        f = User('f')
        g = User('g')
        coach(a, b)
        coach(a, c)
        coach(b, d)
        coach(b, e)
        coach(c, f)
        coach(c, g)
        users = [a, b, c, d, e, f, g]
        limited_infection(users, c, 1, 'parent', maxint)
        self.failUnless(
                        c.get_version() == 1 == a.get_version()
                        )

    def testEleven(self):
        """
        Test #11: Complex Graph Child Limited Infection from middle.
        """
        a = User('a')
        b = User('b')
        c = User('c')
        d = User('d')
        e = User('e')
        f = User('f')
        g = User('g')
        h = User('h')
        i = User('i')
        j = User('j')

    def testTwelve(self):
        """
        Test #12: Complex Graph Parent Limited Infection from middle.
        """
        a = User('a')
        b = User('b')
        c = User('c')
        d = User('d')
        e = User('e')
        f = User('f')
        g = User('g')
        h = User('h')
        i = User('i')
        j = User('j')
        k = User('k')

def main():
    unittest.main()


if __name__ == '__main__':
    main()
