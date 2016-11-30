import math

def factZeros(a):
    trail = 0
    for n in range(5, a+1):
        
        while n:
            
            if n%5 == 0:
                trail += 1
                n = n/5
                
            else:
                break
            
    return trail

#Run-time bounds (Big O):
#O(n)

