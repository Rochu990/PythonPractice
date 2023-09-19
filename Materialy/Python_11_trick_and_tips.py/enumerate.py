data = [1, 2, -3, -4]

for i in range(len(data)):
    if data[i] < 0:
        data[i] = 0

print(data)

for idx, num in enumerate(data):
    if num < 0:
        data[idx] = 0

print(data)