from sqlalchemy import Boolean, Column, Integer, String, create_engine, false
from sqlalchemy.ext.declarative import declarative_base

from app.configuration.settings import database_settings

ficha_ponto_db = create_engine(database_settings())
Base = declarative_base()



class Funcionario(Base):
    __tablename__ = 'funcionarios'

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String(100), nullable=False)
    email = Column("email", String(100), unique=True, nullable=False)
    senha = Column("senha", String(100), nullable=False)
    admin = Column("admin", Boolean, default=false)  # 0 para não admin, 1 para admin


    def __init__(self, nome: str, email: str, senha: str, admin: bool = False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.admin = admin


    