kol_english_children= int(input())
kol_germany_children= int(input())
english_children= set()
germany_children= set()
for i in range(kol_english_children):
    english_children.add(input())
for i in range(kol_germany_children):
    germany_children.add(input())
obshee_children = english_children ^ germany_children
if obshee_children:
    print(len(obshee_children))
else: print("NO")