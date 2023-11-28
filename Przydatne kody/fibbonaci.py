a = 1
b = 2

def fibbonacci(n):
    a = 0
    b = 1
        
    for i in range(1, n + 1):
        a, b = b, a + b
        return b

print(fibbonacci(10)) 

#dodać jaki liste (append)