class Usuario:
    def __init__(self, id, nome, nomeLogin, senha):
        self.idUsuario = id
        self.nome = nome
        self.nomeLogin = nomeLogin
        self.senha = senha

class Animal:
    def __init__(self, id=None, nome=None, idade=None, sexo=None, tipo=None, id_doante=None):
        self.idAnimal = id
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.tipo = tipo
        self.idDoante = id_doante

class Doante:
    def __init__(self, id=None, nome=None, cidade=None, estado=None, telefone=None, email=None):
        self.idDoante = id
        self.nome = nome
        self.cidade = cidade
        self.estado = estado
        self.telefone = telefone
        self.email = email

class Adocao:
    def __init__(self, animal, doante):
        self.animal = animal
        self.doante = doante
