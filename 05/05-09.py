stroka = int(input("Enter a string: "))
nach = False
for i in range(stroka):
    text = input("Enter a text: ")
    if ("кот" or "Кот") in text:
        
        nach = True
        if ("Пес" or "пес") in text:
            nach= False
if nach == True:
    print("МЯУ")
else: print("НЕТ")