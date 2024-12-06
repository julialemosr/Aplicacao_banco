#importar bibliotecas
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, declarative_base

#CONFIGURAR BASE DE DADOS / CRIANDO CONEXÕES ENTRE ELE

#sqlite:///nome.sqlite3 = ao inves de usar 'nome' vai usar o nome do banco de dados
engine = create_engine('sqlite:///nome.sqlite3')
#gerencia sessões com o banco de dados
db_session = scoped_session(sessionmaker(bind=engine))

#o sqlalchemy tem varios tipos de classes e estamos usando a forma declarativa (declarative_base)
Base = declarative_base()
Base.query = db_session.query_property()

#projeto pessoas que tem atividade
class Pessoa(Base):
    #tablename é o nome da tabela
    __tablename__ = 'pessoas'
    #primary_key = chave primária
    #unique= ele é unico
    #nullable= tem que ser preenchido obrigatoriamente
    #String= quantidade de letra
    #index= é para fazer pesquisa
    #column = é as colunas
    # Integer = tipo de dados(texto,número)
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), nullable=False, index=True)
    sobrenome = Column(String(40), nullable=False, index=True)
    cpf = Column(String(11), nullable=False, index=True, unique=True)

    #representação classes

    def __repr__(self):
        # __repr__ é para representar
        #Self= chama a prória entidade(a si próprio)
        #a chave chave {} é usado para subtituir o format
        return '<Pessoa: {} {}>'.format(self.nome, self.sobrenome)

    #função para salvar no banco
    def save(self):
        # o add é para adicionar
        db_session.add(self)
        # o commit é para salvar
        db_session.commit()

    #função para deletar
    def delete(self):
        #o delete é para deletar
        # db_session = sessão de acesso
        db_session.delete(self)
        # o commit é para salvar
        db_session.commit()

    # serialize_user = serve para desmembrar (separar)
    def serialize_pessoa(self):
        dados_user = {
            "id_user": self.id,
            "nome": self.nome,
            "sobrenome": self.sobrenome,
            "cpf": self.cpf,
        }
        return dados_user

class Atividade(Base):
    # tablename é o nome da tabela
    __tablename__ = 'atividades'
    #relationship = relação com duas tabelas (ex:tabela pessoa e tabola atividade)
    # String= quantidade de letra
    # column = é as colunas
    #ForeignKey = chave estrangeira
    id = Column(Integer, primary_key=True)
    nome = Column(String(80))
    pessoa_id = Column(Integer, ForeignKey('pessoas.id'))
    pessoas = relationship('Pessoa')

    # representação classes
    def __repr__(self):
        return '<Atividade: {}>'.format(self.nome)

    def save(self):
        db_session.add(self)
        # o add é para adicionar
        db_session.add(self)
        # o commit é para salvar

    def delete(self):
        # o delete é para deletar
        # db_session = sessão de acesso
        db_session.delete(self)
        # o commit é para salvar
        db_session.commit()

    def serialize_user(self):
        dados_atividades = {
            "id:_atividade": self.id,
            "nome": self.nome,
            "pessoa_id": self.pessoa_id,
        }
        return dados_atividades


#metodo para criar banco
def init_db():
    Base.metadata.create_all(bind=engine)

#executar dentro do arquivo principal(só ele executa)
if __name__ == '__main__':
    init_db()