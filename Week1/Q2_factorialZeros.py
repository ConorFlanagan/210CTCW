import math

def factZeros(a):
    trail = 0
    for n in range(5, a+1):
        
        while n:                #While divisible by 5, the loop will run
            
            if n%5 == 0:        
                trail += 1
                n = n/5         #New value of n if divisible by 5 with no remainder
                
            else:
                break
            
    return trail

#Run-time bounds (Big O):
#O(n)

