word = input("Words: ")
words = word.split(" ")
sentence = input("Sentence: ")
sentence = sentence.split(" ")
for a_word in words:
    j=0
    for letter in a_word:
        if letter in sentence[j]:
            print("Yes")
        else:
            print("No")
        j+=1