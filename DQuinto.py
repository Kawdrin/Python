'''
import struct
nome = 'Kawan'
idade = 17
altura = 1.75
cod = struct.pack('5s I f', nome.encode(), idade, altura)
arq = open('Pessoas.cod', 'wb')
arq.write(cod)
arq.close()
arq = open('Pessoas.cod', 'rb')
cod_ab = arq.readline()
print(cod_ab)
cod_desp = struct.unpack('5s I f', cod_ab)
print(cod_desp)
nome = cod_desp[0].decode()
print(nome)
'''
'''
import struct
t = (b'Kawan', 17, 1.75)
s = struct.Struct('5s I f')
data = s.pack(*t)
print(data)
dados = s.unpack(data)
print(dados[0].split(b'a'))
'''
import struct

class RgInvalidoErro(Exception):
    def __str__(self):
        return 'Digite um RG valido!!'

class CpfInvalidoErro(Exception):
    def __str__(self):
        return 'Digite um CPF valido!!'

def regis(n):
    while True:
        try:
            rg = str(input(f'{n} o seu R.G: '))
            if(len(rg) == 12):
                if('.' == rg[2]) and ('.' == rg[6]) and ('-' == rg[10]):
                    return rg
                else:
                    raise RgInvalidoErro
            else:
                raise RgInvalidoErro
        except RgInvalidoErro:
            print(RgInvalidoErro())

def cpfis(n):
    while True:
        try:
            cpf = str(input(f'{n} o seu CPF:'))
            if(len(cpf) == 14):
                if('.' == cpf[3]) and ('.' == cpf[7]) and ('/' == cpf[11]):
                    return cpf
                else:
                    raise CpfInvalidoErro
            else:
                raise CpfInvalidoErro
        except CpfInvalidoErro:
            print(CpfInvalidoErro())

def salvaDados(nome, rg, cpf):
    arq = open('Dados.zit', 'ab')
    cod = struct.pack(f'{len(nome)}s 12s 14s', nome.encode(), rg.encode(), cpf.encode())
    arq.write(cod)
    arq.write(b'\n')
    arq.close()

def imprimeDados():
    arq = open('Dados.zit', 'rb')
    dados = arq.readlines()
    print(d)
    arq.close()

def main():
    while True:
        print('=-='*10)
        nome = str(input('Digite seu nome: '))
        rg = regis(nome)
        cpf = cpfis(nome)
        salvaDados(nome, rg, cpf)
        esc = str(input('Quer continuar[S/N]?')).upper()
        if(esc == 'N'):
            imprimeDados()
            print('|||<<< ATE LOGO >>>|||')
            break

main()