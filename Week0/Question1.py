def dateCalc(d, m, y):
    monthList = [31,28,31,30,31,30,31,31,30,31,30,31]
    p = 0
    l = 0
    if y%4 == 0:
        e = d
    else:
        e = d - 1
    for i in range(0,m-1):
        p = p + monthList[i]
        if i == (m-2):
            print("Days passed: " + str(p+e))
    print("Days left: " + str(365 - p - e + 1))
    
dateCalc(25,9,2016)
