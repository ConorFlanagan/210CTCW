
def highestFloat(a,b,c,d):
    print(round(max(a/b,c/d,3)))

highestFloat(30,6,20,10)



def triangleRel(a,b,c,p):
    if p[0] > max(a[0],b[0],c[0]):
        print("right")
    else:
        print("left")
    if p[1] > max(a[1],b[1],c[1]):
        print("above")
    else:
        print("below")

#triangleRel([3,4],[0,5],[6,9],[-2,4])



def functionCalc(x):
    if x < -2:
        y = x**2+4*x+4
    if x == 0:
        y = 0
    elif x > -2:
        y = x**2+5*x
    print(y)

#functionCalc(2)


def stringReplace(s,b,l):
    return s.replace(s[b:b+l],"")

#print(stringReplace("beautiful",2,4))



def dateCalc(d, m, y):
    monthList = [31,28,31,30,31,30,31,31,30,31,30,31]
    p = 0
    l = 0
    for i in range(0,m-1):
        p = p+i
