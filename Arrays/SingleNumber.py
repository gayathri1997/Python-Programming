from collections import Counter

a = [1,1,3,4,2,2,3]
count = Counter(a)

for item, value in count.items():
    if value == 1:
        print(item)
