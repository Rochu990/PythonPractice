light = input("Jakie jest światlo? (red, green, yellow, off)")

# if light == 'red':
#     print("Czekaj!")
# elif light == 'yellow':
#     print("Przygotuj się!")
# elif light == 'off':
#     print("Znaki")
# elif light == 'green':
#     print("Jedź")
# else:
#     print("Niewłaściwa komenda")

print("Jedź") if light == 'green' else print("Czekaj")