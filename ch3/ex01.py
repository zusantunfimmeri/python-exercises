#!/usr/bin/env python
# EX 01: create a new list with 3 random strings as elements

import random
import string

def randomstring(times, chars):
    s = ''
    for _ in xrange(times):
        s += random.choice(chars)
    return s

def main():
    lista = []
    for _ in xrange(3):
        stringa = randomstring(random.randint(5, 15), 
                               string.ascii_letters + string.digits )
        lista.append(stringa)
    print(lista)

if __name__ == '__main__':
    main()
