# ile razy wypadnie sześciokrotnie ta nsama strona monety przy 1000 rzutach?
import random

def experiment():
    def coin_toss():
        values = ["R", "O"]
        result = []
        while len(result) < 1000:
            result.append(random.choice(values))
        return result

    def throws_counter():
        coins = coin_toss()
        counter = 0
        result = 0

        for i in range(len(coins) - 1):
            if coins[i] == coins[i + 1]:
                counter += 1
                if counter == 6:
                    result += 1
                    counter = 0
            else:
                counter = 0

        return result

    return throws_counter()


print(experiment())
