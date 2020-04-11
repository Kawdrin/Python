'''
def geraQuadrados(n):
    for i in range(n):
        yield i**2

for i in geraQuadrados(5):
    print(i)
'''
def imprime(n):
    for i in range(n):
        x = yield i**2
        print(x)

z = imprime(5)
print(next(z))
z.send(77)