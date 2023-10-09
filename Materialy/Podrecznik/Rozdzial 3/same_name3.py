
def spam():
    global eggs
    eggs = 'spam'

def bacon():
    eggs = 'bacnon'

def ham():
    print(eggs)

eggs = 42
spam()
print(eggs)