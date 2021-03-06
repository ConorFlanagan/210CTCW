
def increasingSubsequence(a):
    lists = []          #List of increasing subsequences
    new = True
    workList = []       #Current increasing subsequence

    for i in range(0,len(a)):
        if new == True:                         
            workList = []                       #Reset current work list
            workList.append(a[i])
            if a[i+1] > a[i]:
                new = False                     
            elif a[i+1] < a[i]:
                lists.append([workList])        #Append work list to lsit of increasing subsequences
                new = True                      
        elif new == False:                      
            workList.append(a[i])
            if i == len(a)-1:                   #Check for final value
                lists.append(workList)          #Append work list to list of increasing subsequences
                break
            elif a[i+1] > a[i]:
                new = False
            elif a[i+1] < a[i]:
                lists.append(workList)          #Append work list to list of increasing subsequences
                new = True
    print("Sequence: ")
    print(a)
    print(" ")
    print("All increasing subsequences:")       #Print current list of increasing subsequences
    print(lists)
    print("")
    print("Longest increasing subsequence:")
    print(max(lists, key = len))
        
print("Example 1")
print(" ")
increasingSubsequence([1,2,3,4,1,5,1,6,7])
print(" ")
print(" ")
print("Example 2")
print(" ")
increasingSubsequence([1,3,5,6,7,2,4,6,1,2,3,4,5,6,7,8,9])
print(" ")
print(" ")
print("Example 3")
print(" ")
increasingSubsequence([1,2,3,4,1,3,5,6,2,3,4])
print(" ")
print(" ")
print("Example 4")
print(" ")
increasingSubsequence([1,3,5,4,5,7,8,9,4,6,3,1,2,4,7,8,10,11,16,6,8,9,12,13,17,20,1,3,4,7,8,13,15,17,18,20])

