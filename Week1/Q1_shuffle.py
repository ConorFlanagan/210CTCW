import random

def shuf(List):
    for a in range(len(List)-1,0,-1):
        b=random.randint(0,a)
        if b == a:
            continue
        List[a],List[b] = List[b],List[a]
    return (List)

#Run-time bounds (Big O):
#Total = 5n + 2
#O(n)
