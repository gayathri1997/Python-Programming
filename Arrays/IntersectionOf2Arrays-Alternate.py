from collections import Counter

list1 = [1,2,2,1] #[4,9,5]
list2 = [2]

for i in (Counter(list1) & Counter(list2)).elements():
  print(i)
