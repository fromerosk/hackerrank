#!/bin/python3

import math
import os
import random
import re
import sys

def updateFrequencies(hm, new_freq, old_freq):
    nf = None
    try:
        nf = hm[new_freq]
    except:
        pass

    if nf == None:
        hm[new_freq] = [1]
    else:
        nf[0] += 1

    if old_freq != None:
        of = None
        try:
            of = hm[old_freq]
        except:
            pass

        if of == None:
            hm[of] = [1]
        else:
            of[0] -= 1



# Complete the freqQuery function below.
def freqQuery(queries):
    hm = {}
    hm_freq = {}

    count_result = []

    for q in queries:
        num = q[1]

        count = None
        try:
            count = hm[num]
        except:
            pass


        if q[0] == 1:
            if count == None:
                hm[num] = [1]
                updateFrequencies(hm_freq, 1, None)
            else:
                count[0] += 1
                updateFrequencies(hm_freq, count[0], count[0]-1)

    
        if q[0] == 2:
            if count != None and count[0] > 0:
                count[0] -= 1
                updateFrequencies(hm_freq, count[0], count[0]+1)


        if q[0] == 3:
            freq = None
            try:
                freq = hm_freq[q[1]]
            except:
                pass

            if freq != None and freq[0] > 0:
                count_result.append(1)
            else:
                count_result.append(0)
            
    return count_result