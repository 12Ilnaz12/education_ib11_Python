stroka = int(input("Enter a string: "))
nach = 1

while stroka > nach:
    text = input("Enter a text: ")
    if ("кот" or "Кот") in text:
        text = input("Enter a text: ")
        print("МЯУ")
    else:
        text = input("Enter a text: ")
        print("НЕТ")
    nach += 1

