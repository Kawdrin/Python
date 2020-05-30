'''
class NossoContextManager(object):
    def imprime(self, msg):
        print(msg)
    def __enter__(self):
        print('Entrando no bloco with')
        return self
    def __exit__(self, tipo, valor, traceback):
        print(tipo)
        print(valor)
        print(traceback)

with NossoContextManager() as teste:
    teste.imprime('Ola Mundo!')
'''
'''
class NossoContextManager:
    def __enter__(self):
        print('Entramos no bloco with')
    def __exit__(self, tipo, valor, traceback):
        print(tipo)
        print(valor)
        print(traceback)

with NossoContextManager() as nosso:
    raise ValueError('SPAM')
'''
'''
class DeuErroArquivo(Exception):
    def __init__(self, linha, arq):
        self.linha = linha
        self.arq = arq
    def putz(self):
        print('Putz!!!')
    def __str__(self):
        return f'Deu erro na linha {self.linha} do arquivo {self.arq}'

try:
    raise DeuErroArquivo('meu deus', 'Arquivo.txt')
except DeuErroArquivo as E:
    E.putz()
    print(E)
'''
import pdb

def main ():

    pdb.set_trace()
    
    n = int(input("Digite n: "))
    x = float(input("Digite as coordenadas x do ponto 1: "))
    y = float(input("Digite as coordenadas y do ponto 1: "))
    ponto_m = [x,y]
    for i in range (1,n):
        x = float(input("Digite as coordenadas x do ponto %d: "%(i+1)))
        y = float(input("Digite as coordenadas y do ponto %d: "%(i+1)))
        ponto = [x,y]
        if angulo(ponto[0],ponto[1]) < angulo(ponto_m[0],ponto_m[1]):
            ponto_m = ponto
    print (ponto_m)
    
def modulo (y):
    if y < 0:
        y = -y
    return y

def arctan (x):
    k, arctan, n = 1, 0, 0
    while modulo(((x**(k))/k)*((-1)**(n))) >= 0.001:
        arctan += ((x**(k))/k)*((-1)**(n))
        k += 2
        n += 1
    return arctan

def angulo (x,y):
    if y>x:
        angulo = (3.14/2) - arctan(x/y)
    else:
        angulo = arctan(y/x)
    angulo *=(180/3.14)
    return angulo

if __name__ == '__main__':
    main()