open_list =  ['(','{','[']
close_list = [')','}',']']

exp = "{[]{(}}"
stack = []
for i in exp:
    if i in open_list:
        stack.append(i)
    elif i in close_list:
        pos = close_list.index(i)
        if ((len(stack) > 0) and (stack[len(stack)-1] == open_list[pos])):
            stack.pop()
        else:
            print("Unbalanced")
            break
            
if len(stack) == 0:
    print("Balanced")