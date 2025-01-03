def isVowel(ch):
    return ch.upper() in ['A', 'E', 'I', 'O', 'U']
def countVowels(str):
    count=0
    for i in range(len(str)):
        if isVowel(str[i]):
            count=count+1
    return count

str = "Raj Meena"
print("Total Vowels in the string is: ",countVowels(str))