# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps&h_r=next-challenge&h_v=zen

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):

    hm = {}

    count = 0
    for idx in range(len(s)):
        for idx2 in range(idx, len(s)):
            sbs = ''.join(sorted(s[idx:idx2+1]))
            if sbs in hm:
                hm[sbs] += 1
            else:
                hm[sbs] = 1

    for k in hm.keys():
        ct = hm[k]
        count += ct * (ct-1)/2
    return int(count)

if __name__ == '__main__':
    print(sherlockAndAnagrams('kkkk'))
