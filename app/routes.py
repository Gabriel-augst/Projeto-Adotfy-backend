from app import app
from flask import render_template
from app.models.queryFunctions import *

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/quero-adotar')
def quero_adotar():
    listaDeAdocao = buscarAnimais()
    return render_template('quero-adotar.html', lista = listaDeAdocao)

@app.route('/info-animal/<int:idAnimal>')
def info_do_animal(idAnimal):
    informacoesAdocao = infoAnimal(idAnimal)
    return render_template('info-animal.html', info = informacoesAdocao)
