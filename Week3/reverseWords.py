def revWords():
    x = input("Enter string to reverse: ")
    y = list()
    m = ""
    for w in x.split(' '):
        y.insert(0, w)
    for i in y:
         m += i + " "
    print(m)
