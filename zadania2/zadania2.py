from enum import Enum
from file_manager import FileManager
from chuck_norris import ChuckNorris

"""Stwórz funkcję, która jako parametry przyjmuje dwie listy a_list oraz b_list. Następnie zwróć listę, która będzie posiadać parzyste indeksy z listy a_list oraz nieparzyste z b_list."""
def f1(a_list, b_list):
    """lista indeksów, nie wartości - wedle polecenia"""
    wynik = [a for a, b in enumerate(a_list) if a % 2 == 0]
    wynik = wynik + [a for a, b in enumerate(b_list) if a % 2 != 0]

    return wynik
"""
Stwórz funkcję, która przyjmuje parametr data_text, a następnie zwróci następujące informacje o parametrze w formie słownika (dict):

    length: długość podanego tekstu,
    letters: lista znaków w wyrazie np. ['D', 'o', 'g'],
    big_letters: zamieniony parametr w kapitaliki np. DOG
    small_letters: zamieniony parametr w małe litery np. dog
"""
def f2(data_text):
    slownik = {
        "length": len(data_text),
        "letters": [letter for letter in data_text],
        "big_letters": data_text.upper(),
        "small_letters": data_text.lower()
    }

    return slownik

"""Stwórz funkcję, która przyjmie jako parametry text oraz letter, a następnie zwróci wynik usunięcia wszytkich wystąpień wartości w letter z tekstu text."""
def f3(text, letter):
    return text.replace(letter, "")

"""Stwórz funkcję, która przelicza temperaturę w stopniach Celsjusza na Fahrenheit, Rankine, Kelvin. Typ konwersji powinien być przekazany w parametrze temperature_type i uwzględniać błędne wartości."""
class TempTypes(Enum):
    FAHRENHEIT = 1
    RANKINE = 2
    KELVIN = 3


def f4(temperature_in_c, temperature_type):
    if temperature_type == TempTypes.FAHRENHEIT:
        return (temperature_in_c * 1.8000) + 32
    elif temperature_type == TempTypes.RANKINE:
        return (temperature_in_c * 1.8000) + 491.67
    elif temperature_type == TempTypes.KELVIN:
        return temperature_in_c + 273.15
    else:
        return 'Błędny typ temperatury'

"""Stwórz klasę Calculator, która będzie posiadać funkcje add, difference, multiply, divide."""
class Calculator:
    """
    obiekt = Calculator()
    obiekt.add(15, 44)
    obiekt.difference(30, 50)
    ...
    """
    def add(self, x, y):
        return x + y
    
    def difference(self, x, y):
        return x - y
    
    def multiply(self, x, y):
        return x * y
    
    def divide(self, x, y):
        return x / y


"""Stwórz klasę ScienceCalculator, która dziedziczy po klasie Calculator i dodaj dodatkowe funkcje np. potęgowanie."""
class ScienceCalculator(Calculator):
    def potegowanie(self, x, y):
        return x ** y
    def modulo(self, x, y):
        return x % y


"""Stwórz funkcję, która wypisuje podany tekst od tyłu np. koteł -> łetok."""
def reverseString(some_string):
    return some_string[::-1]

"""
Stwórz nowy moduł w projekcie o nazwie file_manager. Stwórz klasę FileManager z parametrem w konstruktorze file_name. Klasa będzie zawierać dwie metody: read_file oraz update_file. Funkcja update_file powinna zawierac parametr text_data, które w efekcie ma być dopisane na końcu pliku. Funkcja read_file powinna zwrócić zawartość pliku.
Zaimportuj klasę FileManager w innym pliku, a następnie zademonstruj działanie klasy.

# Przykład użycia:
fm = FileManager("testowy")
print(fm.update_file('\njakaś treść'))
"""
chuck = ChuckNorris(['Adam', 'Jan', 'Kamil', 'Beata', 'Katarzyna', 'Iwona'])
print(chuck.generate())