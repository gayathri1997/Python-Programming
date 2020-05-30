from itertools import permutations 

a = [54, 546, 548, 60 ]
l = []
for i in permutations(a, len(a)):
    l.append("".join(map(str,i)))

print(max(l))
