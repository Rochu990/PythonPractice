# -Napisz program który poprosi użytkownika o podanie jakiegoś ciągu znaków
# -Następnie ten ciąg znaków podziel po spacji (podpowiedź - poszukaj funkcji "split"
# -Dla każdego słowa policz ilość liter
# -Całość zapisz w pliku "result.txt" (każda nowa linijka powinna mieć format: "<słowo> <ilość liter>",

# Przykład:
# Wejście:
# "ala ma kota"

# Wyjście:
# "ala 3"
# "ma 2"
# "kota 4"

print('Hej! Wprowadź dowolne zdanie!!!')
user_choice = input()

with open('result.txt', 'w') as file:
    for word in user_choice.split():    
        file.write((word + " " + str(len(word)) + "\n").capitalize())


    
 




