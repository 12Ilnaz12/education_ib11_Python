shag_shifr = int(input("Enter shag: "))
word = input("Enter: ")
for i in range(len(word)):
    f = ord(word[i])
    j = f + shag_shifr
    print(chr(j), end="")