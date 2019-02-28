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


# def forOtherRatio(arr, r):
#     hm = {}
#     count = 0

#     for numb_idx in range(len(arr)):
#         numb = arr[numb_idx]
#         # print('numb', numb, 'idx', numb_idx)


#         forming_triplets = []

#         if numb in hm:
#             forming_triplets = hm[numb]

#         next_numb = numb * r

#         if next_numb not in hm:
#             hm[next_numb] = []
#             # print('initializing next', hm)

#         new_next_forming_triplets = []
#         for triplet in forming_triplets:
#             # print('triplet', triplet)
#             if len(triplet) == 2:
#                 count += 1
#                 # nt = triplet[:]
#                 # nt.append(numb_idx)
#                 # print('nt', nt)
#             if len(triplet) < 2:
#                 new_triplet = triplet[:]
#                 new_triplet.append(numb_idx)
#                 new_next_forming_triplets.append(new_triplet)
#                 # print('add next', hm)
        
#         hm[next_numb] += new_next_forming_triplets
        
#         hm[next_numb].append([numb_idx])
#         print('final  numb proc', hm)


#     # print(hm)
#     return int(count)



def forOtherRatio(arr, r):
    hm = {}
    count = 0

    for numb_idx in range(len(arr)):
        numb = arr[numb_idx]
        print('numb', numb, 'idx', numb_idx)

        triplets_counts = { 'ones': 0, 'twos': 0 }
        if numb in hm:
            triplets_counts = hm[numb]
        else:
            hm[numb] = triplets_counts



        next_numb = numb * r

        next_triplets_counts = { 'ones': 0, 'twos': 0 }
        if next_numb in hm:
            next_triplets_counts = hm[next_numb]
        else:
            hm[next_numb] = next_triplets_counts

        count += triplets_counts['twos']
        next_triplets_counts['twos'] += triplets_counts['ones']
        triplets_counts['ones'] += 1

        print('final  numb proc', hm)
    return int(count)


# Complete the countTriplets function below.
def countTriplets(arr, r):
    if r == 1:
        return forRatioOne(arr)
    else:
        return forOtherRatio(arr, r)


if __name__ == '__main__':
    # print(countTriplets([1, 2, 2, 4],2))
    print(countTriplets([1, 2, 2, 4],2))
    # print(countTriplets([1, 1, 1, 1],1))
    # print(countTriplets([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],1))