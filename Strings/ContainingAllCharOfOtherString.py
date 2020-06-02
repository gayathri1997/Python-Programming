s = "ABAACBAB"
t = "ABC"
maxsize = 9223372036854775807
result , start , count ,  min_window = "" , 0 , 0 , maxsize
letter_count = Counter(t)
for end in range(len(s)):
    letter_count[s[end]] -= 1
    if letter_count[s[end]] >= 0:
        count += 1
    while count == len(t):
        if min_window > end - start + 1:
            min_window = end - start + 1
            result = s[start : end + 1]
        letter_count[s[start]] += 1
        if letter_count[s[start]] > 0:
            count -= 1
        start += 1
print(result)
