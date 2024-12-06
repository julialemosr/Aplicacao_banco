#importar biblioteca
from models import Pessoa, db_session
from sqlalchemy import select

#inserir dados na tabela
def inserir_pessoa():
    pessoa = Pessoa (nome=str(input('Nome: ')),
                     sobrenome=str(input('Sobrenome: ')),
                     cpf=str(input('CPF: '))
                     )
    print(pessoa)
    pessoa.save()

def consulta_pessoa():
    var_pessoa = select(Pessoa)
    var_pessoa = db_session.execute(var_pessoa).all()
    print(var_pessoa)


def atualizar_pessoa():
    #selecione o item a ser alterado
    pessoa = select(Pessoa).where(str(input('Nome: ')) == Pessoa.nome)
    var_pessoa = db_session.execute(pessoa).scalar()
    var_pessoa.nome = input('Novo Nome: ')
    var_pessoa.save()


#remove pessoas
def deletar_pessoa():
        pessoa_deletar = input('Quem você deseja deletar?  : ')
        var_pessoa = select(Pessoa).where(pessoa_deletar == Pessoa.nome)
        var_pessoa = db_session.execute(var_pessoa).scalar()
        var_pessoa.delete()


if __name__ == '__main__':

    while True:
        print('menu')
        print('1 - inserir pessoa')
        print('2 - consultar pessoa')
        print('3 - atualizar pessoa')
        print('4 - deletar pessoa')
        print('5 - sair')
        escolha = input('Escolha: ')
        if escolha == '1':
            inserir_pessoa()
        elif escolha == '2':
            consulta_pessoa()
        elif escolha == '3':
            atualizar_pessoa()
        elif escolha == '4':
            deletar_pessoa()
        elif escolha == '5':
            break