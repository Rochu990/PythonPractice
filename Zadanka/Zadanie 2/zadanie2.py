
# -Napisz program który poprosi użytkownika o podanie nazwy pliku
# -Z pliku wczytaj zawartość (tu masz czytanie z pliku - DDeby - 8 rzeczy w Python, które musisz znać!)
# -Następnie całą zawartość podziel po spacji (podpowiedź - poszukaj funkcji "split"
# -Dla każdego słowa policz ilość liter
# -Całość wypisz na ekranie w postaci "<słowo> <ilość liter>",

# Przykład:
# Wejście:
# "file.csv"

# Zawartość pliku
# "ala ma"
# "kota"

# Wyjście:
# "ala 3"
# "ma 2"
# "kota 4"

print("Hej! Podaj nazwę pliku, który chciałbys otworzyć(wraz z rozszerzeniem)")

user_choice = input()

with open(user_choice) as f:
    for line in f:
        # print(line)
        words_list = line.split()
        for i in words_list:
            print(i + " " + str(len(i)))