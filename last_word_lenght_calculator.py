def lenghtLastWord(word):
    lst = word.split()
    lenght_last_word = len(lst[-1])
    return lenght_last_word
    
word = "This is a skae hub developer program"

print(lenghtLastWord(word))