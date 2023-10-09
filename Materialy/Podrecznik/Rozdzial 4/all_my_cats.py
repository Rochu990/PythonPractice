
cat_names = []

while True:
    print('Podaj imię kota ' + str(len(cat_names) + 1) +  
    ' (Ewentualnie nic nie wpisuj, aby zakończyć.): ')
    name = input()
    if name == '':
        break
    cat_names = cat_names + [name]
print('Oto imiona kotów:')
for name in cat_names:
    print(' ' + name)
