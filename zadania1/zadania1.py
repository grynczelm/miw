zmienna = """Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. 
Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. 
Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. 
Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, 
a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na 
komputerach osobistych, jak Aldus PageMaker"""

imie = "Mateusz"
nazwisko = "Grynczel"

print(
    "W tekście jest",
    zmienna.count(imie[2]),
    "liter",
    imie[2],
    "oraz",
    zmienna.count(nazwisko[3]),
    "liter",
    nazwisko[3]
)

zmienna_typu_string = "abcd"

print(dir(zmienna_typu_string))
help(zmienna_typu_string.encode)

print(imie[::-1].capitalize(), nazwisko[::-1].capitalize())

lista = [x for x in range(1, 11)]

lista2 = [lista.pop(5) for _ in range(1, 6)]

lista.extend(lista2)

lista.insert(0, 0)

listaCopy = lista.copy()

lista.sort(reverse=True)

print(lista)

slownik = {
    "145799": {
        "dane": "Mateusz Grynczel",
        "wiek": "50",
        "email": "mateusz@grynczel.it",
        "rokUrodzenia": "1954"
    },
    "131211": {
        "dane": "Jan Kowalski",
        "wiek": "37",
        "email": "jan@kowalskixx54.com",
        "rokUrodzenia": "1980"
    }
}

print(slownik)

numeryTelefonow = ["500500500", "501502503", "800400200", "501502503", "700300300", "700300300"]

print(set(numeryTelefonow))

for i in range(1, 11): print(i)
for i in range(100, 19, -5): print(i)

for el in slownik:
    dane = slownik[el]
    print(
        dane['dane'],
        "(numer indeksu",
        el+")",
        "- wiek:",
        dane['wiek'],
        "lat, urodzony w roku",
        dane['rokUrodzenia']+",",
        "adres e-mail:",
        dane['email']
    )