'''

a^2 = b^2 + c^2

'''

def isTriplet(arr, n) :
    
    for i in range(0,n-2) :
        for j in range (i+1,n) :
            for k in range(j+1,n) :
                x = arr[i]*arr[i] 
                y = arr[j]*arr[j] 
                z = arr[k]*arr[k]  
                
                if( x == y + z or y == x+z or z == y+x) :
                    return 1;
                    
    return 0;
    


arr = [3, 1, 4, 6, 5]

if(isTriplet(arr,len(arr))) :
    print("Yes");
else :
    print("No");
