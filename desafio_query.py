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

resultado = session.query(
    Fornecedor, Produto).join(Produto, Fornecedor.id == Produto.fornecedor_id).all()

for fornecedor, produto in resultado:
    print(fornecedor.nome, produto.nome) 

