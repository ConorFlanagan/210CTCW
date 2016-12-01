def removeVowels(word, count=0):
    vowels = ["a","e","i","o","u"]
    if count == len(vowels):
        print(''.join(word))
    elif count < len(vowels):
        if vowels[count] in word:       #Check if vowel in word
            word.remove(vowels[count])
            removeVowels(word, count)
        else:
            count += 1                  #Move to next vowel
            removeVowels(word, count)
        return word
    
if __name__ == "__main__":
    word = input("Input a word: ")
    word = list(word)
    removeVowels(word)
