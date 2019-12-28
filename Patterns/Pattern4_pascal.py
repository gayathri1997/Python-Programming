'''

1 
1 1 
1 2 1 
1 3 3 1 
1 4 6 4 1

'''

def pattern(n) :
    for i in range(1,n+1) :
         k = 1
         for j in range(1,i+1) :
             print(k,end=" ")
             k = int(k*(i-j)/j);
         print("");
         
n = 5;
pattern(n);