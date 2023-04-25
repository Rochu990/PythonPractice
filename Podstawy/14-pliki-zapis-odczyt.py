file = open("countries_and_capitals.txt", "w+")

countries_and_capitals = {'Poland': 'Warsaw',
                          'Czechia': 'Prague', 'Germany': 'Berlin'}

for country, capital in countries_and_capitals.items():
    file.write(country + "-" + capital + "\n")

file.close

###

file = open("countries_and_capitals.txt")

for lines in file.readlines():
    print(lines.strip())

file.close()