#reversing characters in a string
string = 'gayathri is good girl'
print(string[::-1])

#reversing words in a string
s = string.split(' ');
print(s)

for i in reversed(s):
    print(i)