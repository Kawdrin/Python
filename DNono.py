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
import pickle

def calc(n,p):
    if(n<=5000):
        return (n/p*100)+n
    else:
        return n
def main():
    porc = int(input('Valor porcentual do aumento: '))

    gastos = list(map((lambda x: float(x.replace('\n', ''))), open('gastos.txt', 'r')))
    g_corrigidos = list(map((lambda x: calc(x, porc)), gastos))

    with open('Gastos_Corrigidos.txt', 'w') as arq:
        for g in g_corrigidos:
            arq.write(f'R${g:.2f}\n'.replace('.', ','))

    with open('Lista.obj', 'wb') as arq:
        pickle.dump(gastos, arq)
        pickle.dump(g_corrigidos, arq)

main()