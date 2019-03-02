# https://www.hackerrank.com/challenges/count-triplets-1/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

def forRatioOne(arr):
    hm = {}
    for n in arr:
        if n in hm:
            hm[n] += 1
        else:
            hm[n] = 1

    count = 0
    for n in hm.keys():
        #calculate facts
        c = hm[n]
        count += (c * (c-1) * (c-2)) / 6
    return int(count)   


def forOtherRatio(arr, r):
    hm = {}
    count = 0

    for numb_idx in range(len(arr)):
        numb = arr[numb_idx]
        # print('numb', numb, 'idx', numb_idx)

        num_counts = hm[numb] if numb in hm else { 'two': 0, 'three': 0 }

        count += num_counts['three']

        next_numb = numb * r

        next_num_counts = hm[next_numb] if next_numb in hm else { 'two': 0, 'three': 0 }

        next_num_counts['two'] += 1
        next_num_counts['three'] += num_counts['two']

        hm[next_numb] = next_num_counts

        # print('final  numb proc', hm)
    return int(count)


# Complete the countTriplets function below.
def countTriplets(arr, r):
    if r == 1:
        return forRatioOne(arr)
    else:
        return forOtherRatio(arr, r)


if __name__ == '__main__':
    # print(countTriplets([1, 2, 2, 4],2))
    # print(countTriplets([1, 1, 1, 1],1))
    # print(countTriplets([1,3,9,9,27,81],3))
    # print(countTriplets([1,5,5,25,125],5))
    
    print(countTriplets([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],1))

