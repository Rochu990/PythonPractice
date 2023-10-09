
while True:
    print("Kim jestes?")
    name = input()
    if name != "Przemek":
        continue
    print("Witaj Przemek! Jakie jest haslo?")
    password = input()
    if password == "miecznik":
        break
print("Uzyskano dostęp!")