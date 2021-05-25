def intersection(list1,list2):
    list3 = []
    for value in list1:
        if value in list2:
            list3.append(value);
            list2.remove(value);
    print(list3)

list1 = [1,2,3,4,5,4,4,4,4]
list2 = [2,3,4]

intersection(list1,list2)
