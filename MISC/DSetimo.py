'''
import json
data = {'Nome': 'Kawan', 'RG': 123456789, 'CPF': 12345678910}
data_string = json.dumps(data)
file = open('teste.json', 'wb')
file.write(data_string.encode())
file.close()

file = open('teste.json', 'ab')
dado = [1, 2, 3, 4]
data_s = json.dumps(dado)
file.write(data_s.encode())
data = ('a', 'b', 'c')
data_s = json.dumps(data)
file.write(data_s.encode())
file.close()

file = open('teste.json', 'rb')
data_total = file.readline()

data1 = data_total[:54]
data1 = data1.decode()
obj1 = json.loads(data1)

data2 = data_total[54:66]
data2 = data2.decode()
obj2 = json.loads(data2)

data3 = data_total[66:]
data3 = data3.decode()
obj3 = json.loads(data3)
'''
import pickle
arq = open('arquivo.pck', 'wb')
l1 = [1, 2, 3]
pickle.dump(l1, arq)

class Pessoa(object):
    def __init__(self, n, p):
        self.n = n
        self.p = p
    def ola(self):
        print(f'Ola eu sou {self.n} e peso {self.p}')

pedro = Pessoa('Kawan', 67)
pickle.dump(pedro, arq)
arq.close()

arq = open('arquivo.pck', 'rb')
x = pickle.load(arq)
print(x)
y = pickle.load(arq)
print(y.ola())
z = pickle.dumps(y)
w = pickle.loads(z)
print(w)