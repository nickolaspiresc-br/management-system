# * Gerenciadores de Contexto (with): Crie uma classe de conexão com o banco de dados que use o método __enter__ e __exit__ para abrir e fechar a conexão automaticamente.
#CRUD (Create, Read, Update, Delete): functions, class CRUD
'''
2. O Banco de Dados (SQL e Normalização)
 * Desafio: Em vez de salvar em um arquivo JSON, salve no PostgreSQL.
 * Normalização: Não crie uma tabela única com todos os dados. Crie tabelas separadas para usuarios, livros e emprestimos. Use Chaves Estrangeiras (Foreign Keys) para ligá-las.
 * Queries Complexas:
   * Escreva uma query (usando JOIN) para listar todos os livros que estão atualmente emprestados com o nome do usuário.
   * Crie uma query que mostra os 5 livros mais emprestados (use GROUP BY e COUNT).
'''

#Import modules
import psycopg2
import os
from dotenv import load_dotenv

#Load .env
load_dotenv()

#Connect with server
conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
)

cur = conn.cursor()