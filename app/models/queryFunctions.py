import sqlite3
from classModels import Animal, Doante, Adocao

conn = sqlite3.connect("adocao.db", check_same_thread=False)
cur = conn.cursor()

def buscarAnimais():
    lista = []
    cur.execute('SELECT A.idAnimal, A.nome, A.idade, D.cidade, D.estado FROM animal A INNER JOIN doante D ON A.idDoante = D.idDoante;')
    while True:
        r = cur.fetchone()
        #r = [idAnimal, nome do animal, idade do animal, cidade do doante, estado do doante]
        if r == None:
            break
        animal = Animal(id=r[0], nome=r[1], idade=r[2])
        doante = Doante(cidade=r[3], estado=r[4])
        adocao = Adocao(animal, doante)
        lista.append(adocao)

    return lista

def infoAnimal(idAnimal):
    cur.execute('SELECT A.nome, A.idade, A.sexo, A.tipo, D.nome, D.cidade, D.estado, D.telefone, D.email FROM animal A INNER JOIN doante D ON A.idDoante = D.idDoante WHERE A.idAnimal = ?;', (idAnimal,))
    r = cur.fetchone()
    #r = [nome do animal, idade do animal, sexo do animal, tipo do animal,
    #     nome do doante, cidade do doante, estado do doante, telefone do doante, email do doante,]
    infoAnimal = Animal(nome=r[0], idade=r[1], sexo=r[2], tipo=r[3])
    infoDoante = Doante(nome=r[4], cidade=r[5], estado=r[6], telefone=r[7], email=r[8])
    infoAdocao = Adocao(infoAnimal, infoDoante)

    return infoAdocao

info = infoAnimal(3)
print(f'Nome: {info.animal.nome}')
print(f'Idade: {info.animal.idade}')
print(f'Sexo: {info.animal.sexo}')
print(f'Tipo: {info.animal.tipo}')
print(f'Doante: {info.doante.nome}')
print(f'Cidade: {info.doante.cidade}')
print(f'Estado: {info.doante.estado}')
print(f'Telefone: {info.doante.telefone}')
print(f'Email: {info.doante.email}')

"""
listaAdocao = buscarAnimais()
for itemAdocao in listaAdocao:
    print(f'id: {itemAdocao.animal.idAnimal}')
    print(f'nome: {itemAdocao.animal.nome}')
    print(f'idade: {itemAdocao.animal.idade}')
    print(f'cidade: {itemAdocao.doante.cidade}')
    print(f'estado: {itemAdocao.doante.estado}\n')

SELECT 
    A.idAnimal,
    A.nome,
    A.idade,
    A.sexo,
    A.tipo,
    D.nome,
    D.cidade,
    D.estado,
    D.telefone,
    D.email
FROM 
    animal A INNER JOIN doante D 
ON 
    A.idDoante = D.idDoante;
"""