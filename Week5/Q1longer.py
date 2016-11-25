
def increasingSubsequence(a):
    lists = []          #List of increasing subsequences
    new = True          #Boolean check for increasing value
    workList = []       #Current increasing subsequence

    for i in range(0,len(a)):                   #Main loop iterating through the initial array
        if new == True:                         #Check Boolean
            workList = []                       #Reset current work list
            workList.append(a[i])
            if a[i+1] > a[i]:
                new = False
            elif a[i+1] < a[i]:
                lists.append([workList])
                new = True
        elif new == False:
            workList.append(a[i])
            if i == len(a)-1:
                lists.append(workList)
                break
            elif a[i+1] > a[i]:
                new = False
            elif a[i+1] < a[i]:
                lists.append(workList)
                new = True
    print("All increasing subsequences:")
    print(lists)
    print("Longest Increasing Subsequence:")
    print(max(lists, key = len))
        
print("Example 1")
increasingSubsequence([1,2,3,4,1,5,1,6,7])
print("==========================")
print("Example 2")
increasingSubsequence([1,3,5,6,7,2,4,6,1,2,3,4,5,6,7,8,9])
print("==========================")
print("Example 3")
increasingSubsequence([1,2,3,4,1,3,5,6,2,3,4])
