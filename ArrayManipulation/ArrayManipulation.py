#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0] * (n+2)

    for q in queries:
        arr[q[0]] += q[2]
        arr[q[1]+1] -= q[2]
    biggest = 0

    # nl = list(range(1, n+2))
    for n in list(range(1, n+1)):
        arr[n] += arr[n-1]
        if arr[n] > biggest:
            biggest = arr[n]

    return int(biggest)


    
    