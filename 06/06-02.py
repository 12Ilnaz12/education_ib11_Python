kol_city = int(input())
name_city = set()
last_name_city = set()
for i in range(kol_city):
    name_city.add(input())

last_name_city.add(input())
name_city2 = name_city & last_name_city
if name_city2:
    print("TRY ANOTHER")
else: print("OK")

