
my_pets = ['Zophie', 'Pooka', 'Fat-tail']

print('Podaj imię zwierzaka')
name = input()

if name not in my_pets:
    print('Nie mam zwiarzaka o imieniu ' + name + '.')
else:
    print(name + 'to mój zwierzak.')