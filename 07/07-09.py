word = input("Enter: ")
chislo = int(input("Enter chislo: "))
if len(word) > chislo:
    print(word[chislo-1])
else: print('Ошибка')
