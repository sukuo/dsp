# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
     assert type(count) is int
    if count < 10:
        print('Number of donuts:',+count)
    else:
        print('Number of donuts: many')
    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.

    >>> donuts(4)
    'Number of donuts: 4'
    >>> donuts(9)
    'Number of donuts: 9'
    >>> donuts(10)
    'Number of donuts: many'
    >>> donuts(99)
    'Number of donuts: many'
    """
    raise NotImplementedError


def both_ends(s):
     assert type(s) is str
     if len(s) > 2:
        return (s[:2]+s[-2:])
        elif len(s) < 2:
        return ""
    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.

    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('a')
    ''
    >>> both_ends('xyz')
    'xyyz'
    """
    raise NotImplementedError


def fix_start(s):
     t = list(s)
     counter = 1
     for i in t[1:]:
        if t[counter] == t[0]:
            t[counter] = "*"
        counter += 1
    return "".join(t)

    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.

    >>> fix_start('babble')
    'ba**le'
    >>> fix_start('aardvark')
    'a*rdv*rk'
    >>> fix_start('google')
    'goo*le'
    >>> fix_start('donut')
    'donut'
    """
    raise NotImplementedError


def mix_up(a, b):
     af = a[:2]
     al = a[2:]
     bf = b[:2]
     bl = b[2:]
     return bf2+al + " " + af2+bl
    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.

    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """
    raise NotImplementedError


def verbing(s):
     if len(s) < 3:
         return s
     elif s[-3:] == "ing":
        return s+"ly"
     else:
         return s+"ing"
    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.

    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'
    """
    raise NotImplementedError


def not_bad(s):
    index1 = s.find("not")
    index2 = s.find("bad")
    if "not" in s and "bad" in s and index2 > index1:
        return s[:index1] +""+ "good" +""+ s[(index2+3):]
    else:
        return s
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'

    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    "It's bad yet not"
    """
    raise NotImplementedError


def front_back(a, b):
     if len(a)%2 != 0 and len(b)%2 != 0:
        return a[:int(len(a)/2+1)] + b[:int(len(b)/2+1)]\
        + a[int(len(a)/2+1):] + b[int(len(b)/2+1):]
     elif len(a)%2 !=0 and len(b)%2 == 0:
        return a[:int(len(a)/2+1)] + b[:int(len(b)/2)]\
        + a[int(len(a)/2+1):] + b[int(len(b)/2):]
     elif len(a)%2 == 0 and len(b)%2 != 0:
        return a[:int(len(a)/2)] + b[:int(len(b)/2+1)]\
        + a[int(len(a)/2):] + b[int(len(b)/2+1):]
     else:
        return a[:int(len(a)/2)] + b[:int(len(b)/2)]\
        + a[int(len(a)/2):] + b[int(len(b)/2):]
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back

    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """
    raise NotImplementedError
