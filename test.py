#!/usr/bin/env python3

from roman_numerals import RomanNumeral

class TestRomanNumeral():

    rn2int_values = [
        ('mdcxl', 1640),
        ('mcm', 1900),
        ('md', 1500),
        ('mmmccc', 3300),
        ('mcmc', 2000),
        ('MCMLIV', 1954),
        ('MCMXC', 1990),
        ('MMXIV', 2014),
        ('MCMIII', 1903),
        ('MDCDIII', 1903),
        ('MDCCCCIII', 1903),
        ]

    int2rn_values = [
        ('mdcxl', 1640),
        ('mcm', 1900),
        ('md', 1500),
        ('mmmccc', 3300),
        ('MCMLIV', 1954),
        ('MCMXC', 1990),
        ('MMXIV', 2014),
        ('MCMIII', 1903),
        ]

    def rn2int():
        for roman, int_value in TestRomanNumeral.rn2int_values:
            rn = RomanNumeral(roman)
            assert rn.int == int_value, rn
            assert rn.roman == roman.upper(), rn
        print('Passed rn2int test')

    def int2rn():
        for roman, int_value in TestRomanNumeral.int2rn_values:
            rn = RomanNumeral(int_value)
            assert rn.int == int_value, rn
            assert rn.roman == roman.upper(), rn
        print('Passed int2rn test')

    def test():
        TestRomanNumeral.rn2int()
        TestRomanNumeral.int2rn()


if __name__ == '__main__':
    
    TestRomanNumeral.test()
