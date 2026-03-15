'''
A Estrutura Base (Python, Git e POO)
 * Desafio: Crie classes para Usuario, Livro e Emprestimo.
 * POO: Use a composição. Um Emprestimo não é um Livro; ele contém um Livro e um Usuario.
 * Gerenciadores de Contexto (with): Crie uma classe de conexão com o banco de dados que use o método __enter__ e __exit__ para abrir e fechar a conexão automaticamente.
 * Git: Trabalhe com feature branches. Crie uma branch feature/modelagem-livros, faça o commit, e depois faça um Pull Request para sua branch main (mesmo que seja só você avaliando o próprio código).
2. O Banco de Dados (SQL e Normalização)
 * Desafio: Em vez de salvar em um arquivo JSON, salve no PostgreSQL.
 * Normalização: Não crie uma tabela única com todos os dados. Crie tabelas separadas para usuarios, livros e emprestimos. Use Chaves Estrangeiras (Foreign Keys) para ligá-las.
 * Queries Complexas:
   * Escreva uma query (usando JOIN) para listar todos os livros que estão atualmente emprestados com o nome do usuário.
   * Crie uma query que mostra os 5 livros mais emprestados (use GROUP BY e COUNT).
3. Python Avançado (Decoradores e Geradores)
 * Decoradores: Crie um decorador @log_operacao que imprime no terminal toda vez que um método de "empréstimo" ou "devolução" for chamado.
 * Geradores: Imagine que você tem 1 milhão de logs de empréstimos. Não carregue tudo na memória. Crie um gerador (yield) que lê esses logs linha a linha do banco ou de um arquivo .csv de forma eficiente.
4. Qualidade (Testes com Pytest)
 * Desafio: Crie uma pasta tests/. Para cada classe que você criar, escreva um teste.
 * Integração: Faça um teste que simula o fluxo: 1. Cadastra usuário -> 2. Cadastra livro -> 3. Realiza empréstimo -> 4. Verifica se o banco de dados atualizou o status do livro.
 * Dica: Aprenda a usar Fixtures do Pytest para popular o banco de dados com dados falsos antes de cada teste.
Como estruturar as pastas (O Padrão "Senior" Iniciante)
Para seu projeto no GitHub, organize assim:
meu-projeto/
├── .github/workflows/    # CI/CD (GitHub Actions rodando testes)
├── app/                  # Seu código fonte
│   ├── __init__.py
│   ├── database.py       # Gerenciador de contexto da conexão
│   ├── models.py         # Classes de POO
│   └── services.py       # Lógica de negócio (onde o "trabalho" acontece)
├── tests/                # Testes com Pytest
│   └── test_services.py
├── .env                  # Variáveis de ambiente (credenciais do banco)
├── .gitignore            # O que o Git deve ignorar (venv, .env)
├── requirements.txt      # Dependências do projeto
└── README.md             # Documentação do projeto
'''

#Start
def main():
    print("Working...")

if __name__ == "__main__":
    main()