def checkBit(pattern,arr,  n) : 
    count = 0
      
    for i in range(0, n) : 
        if ((pattern & arr[i]) == pattern) : 
            count = count + 1
    return count 
  
def maxAND (arr,  n) : 
    res = 0
    for bit in range(31,-1,-1) : 
        count = checkBit(res | (1 << bit), arr, n) 

        if ( count >= 2 ) : 
            res =res | (1 << bit) 
              
    return res 


n=int(input())
a=list(map(int,input().split()))
print(maxAND(a,n))

