def binarySearch(L, low, high):
    i = 0
    b = len(L) - 1
    found = False
    
    while i <= b and found == False:
        m = (i+b)//2
        if low <= L[m] <= high:
            found = True
        else:
            if low < L[m]:
                b = m - 1
            else:
                i = m + 1
    return found

print(binarySearch([2,3,4,7,9,13], 10, 14))
