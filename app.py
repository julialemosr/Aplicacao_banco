from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy import select
from models import Pessoa,db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

@app.route('/')
def inicio():
    return render_template('base.html')

@app.route('/pessoa')
def pessoa():
    var_conteudo = 'Será exibido no arquivo base'
    return render_template('pessoa.html',
                           var_conteudo=var_conteudo)

@app.route('/pessoas', methods=['POST', 'GET'])
def pessoas():
    sql_pessoas = select(Pessoa)
    resultado_pessoas = db_session.execute(sql_pessoas).scalars()
    lista_pessoas = []
    for n in resultado_pessoas:
        lista_pessoas.append(n.serialize_pessoa())
        print(lista_pessoas[-1])
    return render_template("lista_pessoa.html",
                           lista_pessoas=lista_pessoas)

@app.route('/tabela_pessoa', methods=['POST', 'GET'])
def tabela_pessoa():
    sql_pessoas = select(Pessoa)
    resultado_pessoas = db_session.execute(sql_pessoas).scalars()
    lista_pessoas = []
    for n in resultado_pessoas:
        lista_pessoas.append(n.serialize_pessoa())
        print(lista_pessoas[-1])
    return render_template("tabela_pessoa.html",
                           lista_pessoas=lista_pessoas)

@app.route('/nova_pessoa', methods=['POST', 'GET'])
def criar_pessoa():
    if request.method == "POST":
        if not request.form['form-nome']:
            flash("Preencher todos os campos", "error")
        else:
            form_evento = Pessoa(nome=request.form['form-nome'],
                                 sobrenome=request.form['form-sobrenome'],
                                 cpf=request.form['form-cpf']
                                 )
            print(form_evento)
            form_evento.save()
            db_session.close()
            flash("PESSOA ADICIONADA COM SUCESSO!!", "success")
            return redirect(url_for('pessoas'))

    return render_template('nova_pessoa.html')


if __name__ == '__main__':
    app.run(debug=True)