from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.exc import SQLAlchemyError


Base = declarative_base()

class Fornecedor(Base):
    __tablename__ = 'fornecedores'

    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    telefone = Column(String(20))
    email = Column(String(50))
    endereco = Column(String(100))

class Produto(Base):
    __tablename__ = 'produtos'

    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    descricao = Column(String(200))
    preco = Column(Integer)
    fornecedor_id = Column(Integer, ForeignKey('fornecedores.id'))

    # estabelece a relação do produto com o fornecedor
    fornecedor = relationship('Fornecedor') #, back_populates='produtos')


engine = create_engine('sqlite:///desadio.db', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session(bind=engine)
# inserindo fornecedores
try:
    with Session() as session: # usando with para gerenciar corretamento o contexto de sessão
        fornecedores = [
            Fornecedor(nome='Fornecedor A', telefone='(11) 1234-5678', email='HbMx4@example.com', endereco='Rua A, 123'),
            Fornecedor(nome='Fornecedor B', telefone='(22) 9876-5432', email='2kqTc@example.com', endereco='Rua B, 456'),
            Fornecedor(nome='Fornecedor C', telefone='(33) 5555-5555', email='3rjT0@example.com', endereco='Rua C, 789')
        ]
        session.add_all(fornecedores)
        session.commit()
except SQLAlchemyError as e: # tratando erros
    print(f"Ocorreu um erro ao inserir os fornecedores: {e}")

# inserindo produtos
try:
    with Session() as session:
        produtos = [
            Produto(nome='Produto A', descricao='Descrição do produto A', preco=100, fornecedor=fornecedores[0]),
            Produto(nome='Produto B', descricao='Descrição do produto B', preco=200, fornecedor=fornecedores[1]),
            Produto(nome='Produto C', descricao='Descrição do produto C', preco=300, fornecedor=fornecedores[2])
        ]
        session.add_all(produtos)
        session.commit()
except SQLAlchemyError as e:
    print(f"Ocorreu um erro ao inserir os produtos: {e}")

