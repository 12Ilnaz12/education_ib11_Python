word = input("Enter: ")
a = True
while a == True:
    word2 = input("Enter: ")
    if word[-1] == word2[0]:
        word = word2
    else: print(word2)