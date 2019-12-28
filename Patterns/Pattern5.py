'''
                     1        
                2        7        
            3        8        12        
        4        9        13        16        
    5        10        14        17        19        
6        11        15        18        20        21

'''

def pattern(n) :
    for i in range(1,n+1) :
        
        for j in range(i,n+1) :
            print(end=" ");
        
        t = i;
        for k in range(1,i+1) :
            print(t,end = " ");
            t = t + n - k;
            
        print();
         
n = 5;
pattern(n);