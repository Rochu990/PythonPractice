import random
secret_number = random.randint(1, 20)
print('Mam na myśli pewną liczbę z zakresu od 1 do 20.')

for guesses_taken in range(1, 7):
    print('Spróbuj odgadnąć liczbę.')
    guess = int(input())

    if guess < secret_number:
        print('Podana liczba jest za mała.')
    elif guess > secret_number:
        print('Podana liczba jest za duża.')
    else:
        break

if guess == secret_number:
    print('Doskonale! Odgadłeś liczbę w ciągu ' + str(guesses_taken) + ' prób!')
else:
    print('Nie udało się! Liczbą, którą miałem na mysli to ' + str(secret_number))