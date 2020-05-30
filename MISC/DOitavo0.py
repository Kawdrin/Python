"""
iter()
next()
"""
'''
#Compress~ao Geral
#/l = [x + 10 for x in range(10)]
#--------------------------------------------------
#Compress~ao em Arquivos:
#/l = [linha.rstrip() for linha in open('teste.txt')]
#--------------------------------------------------
#from random import randint
#l = [randint(1, 100) for i in range(30) if i%2==0]
#l = [randint(1, 100) for i in range(30)]
#l = [x for x in l if x%2==0]
#--------------------------------------------------
l = [x + y + z for x in 'abc' for y in 'lmn' for z in 'xyz']
print(l)
'''
'''
from random import randint
pessoas = int(input('Digite o numero de pessoas: '))
rep = int(input('Numero de repetiç~oes: '))
favo = 0
l = [[f'{randint(1, 30)}/{randint(1, 12)}/{randint(1990, 2020)}' for data in range(pessoas)] for reps in range(rep)]
for lista in l:
    for data in lista:
        a = lista[:]
        a.remove(data)
        if(data in a):
            favo += 1
            break      
            
print(f'Porcentagem: {favo/rep*100}')
'''
'''
l1 = ['Ovos', 'Presunto', 'Frange']
l2 = [5, 2, 13]
a = zip(l1, l2)
print(a)
print(dict(a))
'''