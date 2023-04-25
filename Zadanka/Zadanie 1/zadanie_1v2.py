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
print('Hej! Wprowadź dowolne zdanie!!!')

user_choice = input()
words_list = user_choice.split()

for word in words_list:
    print(word + " " + str(len(word)))