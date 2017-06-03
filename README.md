# Roman Numerals

Convert from and to roman numerals in Python.

# Usage

This package contains a single class, which can be initialised with either an
integer, or a string representing a roman numeral. The resulting `RomanNumeral`
objects have two tags, `.roman` and `.int`, containing the roman and arabic
representation of the number, respectively.

~~~python
>>> rn = RomanNumeral('MDCXLII')
>>> rn, rn.roman, rn.int
(<RomanNumeral MDCXLII (1642)>, 'MDCXLII', 1642)
>>> rn = RomanNumeral(1954)
>>> rn, rn.roman, rn.int
(<RomanNumeral MCMLIV (1954)>, 'MCMLIV', 1954)
~~~

# License

Copyright (c) 2017 Gabriel Pelouze

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
