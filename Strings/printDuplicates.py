#using dictionaries 
#key as variable
#value as number of occurence of the variable


count_dict = {}
string = 'Geeks for geeks'
string = string.lower()

for i in string:
    if i in count_dict.keys():
        count_dict[i] = count_dict[i] + 1
    else:
        count_dict[i] = 1

for k, v in count_dict.items():
    if v > 1 and k != ' ':
        print(k + ' : '  + str(v))