def prime(num, count=2):
    if num <= 1 or num == count:    #0, 1 and 2 are prime, for recursions number is divisible by itself
        return True
    elif (num%count) == 0:
        return False
    else:
        return prime(num,counter+1) #Re-call function with larger count value