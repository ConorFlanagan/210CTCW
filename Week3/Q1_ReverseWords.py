def revWords():
    initial = input("Enter string to reverse: ")
    wordList = list()
    revList = ""
    for w in initial.split(' '):        #Split string into words using spaces to identify words
        wordList.insert(0, w)           #Insert word at start of the list
    for i in wordList:
         revList += i + " "             #Add each word to reverse list
    print(revList)
    revWords()

if __name__ == "__main__":
    revWords()
