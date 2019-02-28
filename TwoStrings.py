# https://www.hackerrank.com/challenges/two-strings/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    hm = {}
    for l in list(s1):
        hm[l] = 1

    for l in list(s2):
        if l in hm:
            return 'YES'
            

    return'NO'

if __name__ == '__main__':
    print(twoStrings('hello','wrd'))