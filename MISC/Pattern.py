from functools import singledispatch

def Direita(object):
    ...

def Esquerda(object):
    ...

def Cima(object):
    ...

def Baixo(object):
    ...


@singledispatch
def key(evento):
    ...

@key.register(Esquerda)
def movimento(evento):
    print('Heroi se moveu para Esquerda!')

@key.register(Direita)
def movimento(evento):
    print('Heroi se moveu para Direita!')

@key.register(Cima)
def movimento(evento):
    print('Heroi Pulou!')
