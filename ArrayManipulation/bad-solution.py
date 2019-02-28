# This solution does not work, fails and timeout


#!/bin/python3

import math
import os
import random
import re
import sys

def findBigger(newValue, acTualBigger):
    return newValue if newValue > acTualBigger else acTualBigger


# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    # print (queries)

    ranges = [[1, n, 0]]
    biggest = 0

    for q in queries:
        temp_ranges = []

        for r in ranges:
            if q[0] <= r[1] and q[1] >= r[0]:
                if q[0] == r[0]:
                    if q[1] == r[1]:
                        #q-------
                        #r-------
                        temp_ranges.append([q[0], q[1], q[2]+r[2]])
                        biggest = findBigger(q[2]+r[2], biggest)
                    elif q[1] > r[1]:
                        #q-----------
                        #r-------
                        temp_ranges.append([q[0], r[1], q[2]+r[2]])
                        biggest = findBigger(q[2]+r[2], biggest)
                        temp_ranges.append([r[1]+1, q[1], q[2]])
                    elif q[1] < r[1]:
                        #q-------
                        #r-----------
                        temp_ranges.append([q[0], q[1], q[2]+r[2]])
                        biggest = findBigger(q[2]+r[2], biggest)
                        temp_ranges.append([q[1]+1, r[1], r[2]])

                elif q[0] < r[0]:
                    if q[1] == r[1]:
                        #q-----------
                        #r   --------
                        temp_ranges.append([q[0], r[0]-1, q[2]])
                        temp_ranges.append([r[0], r[1], q[2]+r[2]])
                        biggest = findBigger(q[2]+r[2], biggest)
                    elif q[1] > r[1]:
                        #q-----------
                        #r   -----
                        temp_ranges.append([q[0], r[0]-1, q[2]])
                        temp_ranges.append([r[0], r[1], q[2]+r[2]])
                        biggest = findBigger(q[2]+r[2], biggest)
                        temp_ranges.append([r[1]+1, q[1], q[2]])
                    elif q[1] < r[1]:
                        #q-----------
                        #r   -----------
                        temp_ranges.append([q[0], r[0]-1, q[2]])
                        temp_ranges.append([r[0], q[1], q[2]+r[2]])
                        biggest = findBigger(q[2]+r[2], biggest)
                        temp_ranges.append([q[1]+1, r[1], r[2]])

                elif q[0] > r[0]:
                    if q[1] == r[1]:
                        #q    --------
                        #r------------
                        temp_ranges.append([r[0], q[0]-1, r[2]])
                        temp_ranges.append([q[0], q[1], q[2]+r[2]])
                        biggest = findBigger(q[2]+r[2], biggest)
                    elif q[1] > r[1]:
                        #q    --------
                        #r--------
                        temp_ranges.append([r[0], q[0]-1, r[2]])
                        temp_ranges.append([q[0], r[1], q[2]+r[2]])
                        biggest = findBigger(q[2]+r[2], biggest)
                        temp_ranges.append([r[1]+1, q[1], q[2]])
                    elif q[1] < r[1]:
                        #q    --------
                        #r---------------
                        temp_ranges.append([r[0], q[0]-1, r[2]])
                        temp_ranges.append([q[0], q[1], q[2]+r[2]])
                        biggest = findBigger(q[2]+r[2], biggest)
                        temp_ranges.append([q[1]+1, r[1], r[2]])

            else:
                temp_ranges.append(r)
        
        ranges = temp_ranges
    return biggest


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
