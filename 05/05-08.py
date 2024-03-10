coshka_v_stroke = False
text = ""
kol_strokes = 0
number_cot = 0
kolich_cats = 0
while "СТОП" != text:
    text = input("Enter a text: ")
    kol_strokes += 1
    if ('Кот' in text) or ('кот' in text):
        coshka_v_stroke = True
        kolich_cats += 1
        if coshka_v_stroke:
            number_cot = kol_strokes

if coshka_v_stroke:
    print(kolich_cats,number_cot)
else: print(0,"-1")