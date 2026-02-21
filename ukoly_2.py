jmeno = "Diana"
print(type(jmeno))


vek = 18
print(type(vek))
vek_float = float(vek)

print(vek)
print(vek_float)


seznam = [3, 8, 1]
print(seznam[1])
seznam.append(381)
print(len(seznam))


slovnik = {
    "jmeno": jmeno,
    "vek": vek
}
print(slovnik["jmeno"])
slovnik["mesto"] = "Almaty"
print(slovnik.keys())


cislo = "5"
cislo_int = int(cislo)
print(cislo)
print(cislo_int)


boolean = True
print(type(boolean))


prazdny_list = []
print(type(prazdny_list))


cislo1 = 5
cislo2 = 5
print(id(cislo1))
print(id(cislo2))


retezec1 = "ahoj"
retezec2 = "ahoj"
print(id(retezec1))
print(id(retezec2))


seznam1 = [1, 2, 3]
seznam2 = [1, 2, 3]
print(id(seznam1))
print(id(seznam2))


slovnik1 = {"jmeno": "Jan", "vek": 30}
slovnik2 = slovnik1
print(id(slovnik1))
print(id(slovnik2))

slovnik1["mesto"] = "Ostrava"
print(slovnik2)


seznam = [1, 2, 3, 4, 5]
novy_seznam = seznam[1::2]

novy_seznam[0] = 10
print(seznam)


seznam = [1, 2, 3]
print(id(seznam))

seznam[1] = 5
print(id(seznam))


retezec = "ahoj"
retezec = "A" + retezec[1:]
print(retezec)




x_int = 5
y_int = 3
x_float = 5.5
y_float = 2.0
x_str = "Hello"
y_str = "World"
x_bool = True
y_bool = False
x_list = [1, 2]
y_list = [3, 4]

print(x_int + y_int) 
print(x_int + x_float) 
print(x_float - y_float)
print(x_str + y_str)
print(x_bool + y_bool)
print(x_bool + 9) 
print(x_list + y_list) 


cislo = -10
if cislo >= 0:
     absh = cislo 
else:
     absh = -cislo
print(absh)



