'''
def geraQuadrados(n):
    for i in range(n):
        yield i**2

for i in geraQuadrados(5):
    print(i)
'''
'''
def imprime(n):
    for i in range(n):
        x = yield i**2
        print(x)

z = imprime(5)
print(next(z))
z.send(77)
'''
'''
def calcCome(pos, tab):
    fixotab = [[n for n in range(len(tab[0]))]for x in range(len(tab))]
    tem = 0
    r = 0
    for i in range(len(tab)*len(tab)):
        for xy in pos:
            posl = xy[0]
            posc = xy[1]
            for nl, l in enumerate(tab):
                for nc, c in enumerate(l):
                    # Verifica a Rainha
                    if(posl == nl) and (posc == nc):
                        fixotab[nl][nc] = 'R'
                    # Calc Vertical-Horizontal
                    elif((posl == nl) or (posc == nc)) and (fixotab[nl][nc] != fixotab[posl][posc]):
                        if(fixotab[nl][nc] == 'R'):
                            tem+=1
                    # Calc \Diagonais/
                    elif((nc+nl == posl+posc) or (nl-nc == posl-posc)) and (fixotab[nl][nc] != fixotab[posl][posc]):
                        if(fixotab[nl][nc] == 'R'):
                            tem+=1
            if(tem >= 1):
                fixotab[posl][posc] = f'X'
            else:
                fixotab[posl][posc] = f'R'
            tem = 0

    print(fixotab)
    print('-'*50)
    for l in fixotab:
        for c in l:
            if(c == 'R'):
                r+= 1
                if(r >= 8):
                    print('AQUUIIQWEIJQWIODJASOID')
                print(f'\033[1;34m| \033[1;33mR ', end='')
            else:
                print(f'\033[1;34m| \033[1;31mX ', end='')
        print(f'\033[1;34m |')

def imprimiTab(t):
    for nl, l in enumerate(t):
        for nc, c in enumerate(l): 
            yield nl, nc

def main():a
    n = int(input('Tamanho do tabuleiro: '))
    tab = [[x for x in range(n)] for y in range(n)]
    pl = imprimiTab(tab)
    pl = list(iter(pl))
    lista = list()
    for x in range(n*n):
        lista.append([pl[x][0], pl[x][1]])
    rai = 0
    while(rai != 8):
        rai = calcCome(lista, tab)
        try:
            lista.pop(0)
        except:
            print('N~ao tem como colocar 8 rainhas nesse tabuleiro!!!')
            break

main()
'''
palavra = input("Digite a palavra que você deseja permutar\n")

#Obtemos as permutações a partir do seguinte algoritmo
permutações = (palavra[i:].lower() + palavra[:i].lower() for i in range(len(palavra)))

#Agora precisamos eliminar as permutações repetidas
lista = []
for perm in permutações:
    if perm not in lista:
        lista.append(perm)

#E por último imprimimos a lista
print(lista)
