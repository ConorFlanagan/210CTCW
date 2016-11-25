import random

def shuf(List):
    newLen = len(List)                      #1
    for a in range(newLen,0,-1):            #n
        b=random.randint(0,a)               #n
        if b == a:                          #n
            continue                        #n
        List[a],List[b] = List[b],List[a]   #n
    print(List)                             #1

shuf([5,3,8,6,1,9,2,7])

#Total = 5n + 2
#O(n)
