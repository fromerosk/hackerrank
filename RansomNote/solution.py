# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    hm = {}
    for word in note:
        if word in hm:
            hm[word] += 1
        else:
            hm[word] = 1

    for word in magazine:
        if word in hm:
            hm[word] -= 1
            if hm[word] == 0:
                hm.pop(word)
        
    if len(hm.keys()) > 0:
        print('No')
    else:
        print('Yes')