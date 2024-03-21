# -Napisz program który poprosi użytkownika o podanie jakiegoś ciągu znaków
# -Następnie ten ciąg znaków podziel po spacji (podpowiedź - poszukaj funkcji "split"
# -Dla każdego słowa policz ilość liter
# -Całość wypisz na ekranie w postaci "<słowo> <ilość liter>",

# Przykład:
# Wejście:
# "ala ma kota"

# Wyjście:
# "ala 3"
# "ma 2"
# "kota 4"

# -----------------------------------------------
# Zadanie 5:
# Zrefaktoryzuj zadania 1-4, tak żeby:
# a) wszystkie korzystały z funkcji z zadania 4 (powinny ją importować)

from zadanie_4 import fun

print("Hej! Wprowadź dowolne zdanie!!!")

user_choice = input()
words_list = user_choice.split()

# for word in words_list:
#     print((word + " " + str(len(word))).capitalize())

print(fun(words_list))
