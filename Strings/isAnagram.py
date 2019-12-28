string1 = 'abcdefg'
string2 = 'gfedcba'

if sorted(string1) == sorted(string2):
    print('anagram')
else:
    print('not anagram')
