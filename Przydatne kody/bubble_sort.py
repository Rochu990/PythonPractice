
def bubble(data):

    new_data = len(data)

    while new_data > 1:

        for i in range(0, new_data - 1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]

        new_data -= 1
        print(data)

    return data





