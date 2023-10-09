countries_and_capitals = {'Poland': 'Warsaw',
                          'Czechia': 'Prague', 'Germany': 'Berlin'}


try:
    print(2 / 0)
    print(countries_and_capitals['USA'])
except KeyError:
    print("Błąd, brak danych")
except:
    print("Błąd, nie można dzielić przez 0")

