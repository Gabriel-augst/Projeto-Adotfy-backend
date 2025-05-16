import sqlite3

conn = sqlite3.connect("adocao.db", check_same_thread=False)
cur = conn.cursor()

def buscarNomesAnimais():
    cur.execute('SELECT A.idAnimal, A.nome, D.cidade, D.estado FROM animal A INNER JOIN doante D ON A.idDoante = D.idDoante;')
    lista_de_animais = cur.fetchall()

    return lista_de_animais

def infoAnimal(id):
    cur.execute('SELECT A.nome, A.idade, A.sexo, A.tipo, D.nome, D.cidade, D.estado, D.telefone, D.email FROM animal A INNER JOIN doante D ON A.idDoante = D.idDoante WHERE A.idAnimal = ?;', (id,))
    infoDoAnimal = cur.fetchone()

    return infoDoAnimal

#print(buscarNomesAnimais())
#print(infoAnimal(1))


"""
SELECT A.nome, A.idade, A.sexo, A.tipo, D.nome, D.cidade, D.estado, D.telefone, D.email FROM animal A INNER JOIN doante D ON A.idDoante = D.idDoante WHERE A.idAnimal = ?;

"""