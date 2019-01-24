# cc=[('red',3),('green',5),('blue',7),('black',9)]
# name='red'
# for x in cc:
#     if name ==x[0]:
#         code=x[1]
#         print(x)
# print(code)
protseq = input("Protein sequence: ").upper()
protdeg = {"A": 4, "C": 2, "D": 2, "E": 2, "F": 2, "G": 4, "H": 2,
           "I":3, "K": 2, "L": 6, "M": 1, "N": 2, "P": 4, "Q": 2,
           "R": 6, "S": 6, "T": 4, "V": 4, "W": 1, "Y": 2}
segsvalues = []
for aa in range(len(protseq)):
    segment = protseq[aa:aa + 15]
    degen = 0
    if len(segment) == 15:
        for x in segment:
            degen += protdeg.get(x, 3.05)
            segsvalues.append(degen)
    else:
        pass
min_value = min(segsvalues)
minpos = segsvalues.index(min_value)
print(protseq[minpos:minpos+15])
