def recoverSecret(triplets):
    'Add a letter if it is only in the first line.'
    res = ''
    while triplets != []:
        non_firsts = [num for t in triplets for num in t[1:]]
        firsts = [t[0] for t in triplets]
        for f in firsts:
            if f not in non_firsts:
                res += f
                for t in triplets:
                    if t[0] == f:
                        t.pop(0)
                break
        triplets = [t for t in triplets if t != []]
    return res


secret = "whatisup"
triplets = [
    ['t', 'u', 'p'],
    ['w', 'h', 'i'],
    ['t', 's', 'u'],
    ['a', 't', 's'],
    ['h', 'a', 'p'],
    ['t', 'i', 's'],
    ['w', 'h', 's']
]

print(recoverSecret(triplets))
