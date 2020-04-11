'''
def valor(x):
    if(x%2==0):
        return x

a = filter((lambda x: x%2==0), range(5))
print(a)
print(list(a))
print([x**2 for x in range(5) if x%2==0])
print(list(map((lambda x: x**2), filter((lambda x: x%2==0), range(5)))))
'''
'''
def corta(l):
    produtos = list()
    preco = list()
    for p in l:
        p = p.replace('\n', '')
        p = p.split('-')
        produtos.append(p[0].strip())
        preco.append(p[1].strip())
    return dict(zip(produtos, preco))

lista_mercado = open('mercado.txt', 'r')
lista = lista_mercado.readlines()
lista_mercado.close()

lista_mercado = open('nova.txt', 'w')
lista_mercado.write(f'| {"PRODUTO":^25} | {"PREÇO":^9} |\n')
for k, v in corta(lista).items():
    lista_mercado.write(f'| {k:^25} | R${v:<7} |\n')
lista_mercado.close()
'''
'''
import pickle

def main():
    porc = int(input('Valor porcentual do aumento: '))

    gastos = list(map((lambda x: float(x.replace('\n', ''))), open('gastos.txt', 'r')))
    g_corrigidos = list(map((lambda x: (x/porc*100)+x), gastos))

    with open('Gastos_Corrigidos.txt', 'w') as arq:
        for g in g_corrigidos:
            arq.write(f'R${g:.2f}\n'.replace('.', ','))

    with open('Lista.obj', 'wb') as arq:
        pickle.dump(gastos, arq)
        pickle.dump(g_corrigidos, arq)

main()
'''
'''
import pickle

def main():
    #Define o limite
    limite = float(input('Digite um valor limite de correç~ao: '))
    #Ordena as listas do arquivo Lista.obj
    with open('Lista.obj', 'rb') as arq:
        g_anterior = pickle.load(arq)
        g_c_anterior = pickle.load(arq)
    #Cria lista
    lista_correcao = list(filter((lambda x: x <= limite), map((lambda x, y: y-x), g_anterior, g_c_anterior)))
    #Soma os n'umeros
    print(f'A soma dos valores no limite da correç~ao R${sum(lista_correcao):.2f}')

main()
'''
'''
import functools

def olhe_soma(x, y):
    print(f'Adicionando |{x}| a |{y}|')
    return x+y

p = str(input('Digite um palavra: '))
print(functools.reduce(olhe_soma, p))
'''
'''
def verificar(text):
    while True:
        try:
            esc = int(input(text))
            if(1<=esc<=3):
                return esc
            else:
                raise ValueError
        except ValueError:
            print('ERRO! Digite um valor valido!')

def main():
    while True:
        print('-=-'*20)
        esc = verificar('1 - Definir Senha\n2 - Verificar Usuario\n3 - Sair\nOpç~ao: ')
        print('-=-'*20)
        if(esc == 1):
            try:
                senha = int(input('Senha: '))
            except:
                print('Erro!')
            else:
                senha = str(senha)
        elif(esc == 2):
            try:
                v_senha = int(input('Digite sua senha: '))
            except:
                print('Erro!')
            else:
                v_senha = str(v_senha)
                verifica = all(list(map((lambda ns, nv: ns==nv and len(senha)==len(v_senha)), senha, v_senha)))
                if verifica:
                    print('Logado com sucesso!!!')
                else:
                    print('Senha Invalida!')
        elif(esc == 3):
            print('Ate logo...')
            break
        else:
            print('ERRO! Digite um valor valido!')

main()
'''
'''
from random import randint

def calc(n):
    if(n < 3):
        return True
    else:
        return False

vezes = int(input('Lança nº vezes? '))
jogadas = [calc(randint(1, 6)) for v in range(vezes)]
if any(jogadas):
    print(f'A Probabilidade de cair 1 numero menor que 3...\n==>1/{vezes}\n==>Total:{jogadas.count(True)}/{vezes}')
else:
    print(f'A Probabilidade foi 0/{vezes}')
'''
'''
import functools

m = functools.reduce((lambda y=0, x=0: y if int(y.replace('\n', ''))>int(x.replace('\n', '')) else x), open('nums.txt', 'r'))
print(f'O maior numero e:{m}')
'''