import math
def factZeros(a):
    zeros = 0                                   #1
    factorial = math.factorial(a)               #1
    print("Factorial Value:", factorial)        #1
    while factorial > 0:                        #n
        if factorial%10 == 0:                   #n
            zeros += 1                          #n
            factorial = factorial/10            #n
        else:                                   #n
            break                               #n
    print("Trailing Zeros: " + str(zeros))


#O(n)

