import dbm
db = dbm.open('contatos.db', 'c')
db['Kawan'] = 'Kawan.inf@gmail.com'
db['Joao'] = 'joao@gmail.com'
for k in db:
    print(k)