num_home1= set()
num_home2= set()

while True:
    chislo = input()
    if chislo:
        num_home1.add(int(chislo))
    else: break
while True:
    chislo = input()
    if chislo:
        num_home2.add(int(chislo))
    else: break
num_home3 = num_home1 & num_home2
if  not num_home3:
    print("EMPTY")
else: print(num_home3)


