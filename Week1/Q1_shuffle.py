import random

def shuf(List):
    
    for a in range(len(List)-1,0,-1):       #For each index of array
        b=random.randint(0,a)               #Selects random second index
        if b == a:
            continue
        List[a],List[b] = List[b],List[a]   #Swap selected indexes
        
    return (List)

#Run-time bounds (Big O):
#O(n)
