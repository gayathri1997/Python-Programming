string = 'Gayathri dgays dsydg sdsd dh asdfghj'
string = string.lower();
string1 = ''

count_dict = {}

for i in string:
    if i not in string1:
        string1 = string1 + i
        
print(string1)
