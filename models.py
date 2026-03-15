#Desafio: Crie classes para Usuario, Livro e Emprestimo.
# * POO: Use a composição. Um Emprestimo não é um Livro; ele contém um Livro e um Usuario.
# * Gerenciadores de Contexto (with): Crie uma classe de conexão com o banco de dados que use o método __enter__ e __exit__ para abrir e fechar a conexão automaticamente.
# * Git: Trabalhe com feature branches. Crie uma branch feature/modelagem-livros, faça o commit, e depois faça um Pull Request para sua branch main (mesmo que seja só você avaliando o próprio código).

#Crie a classe Livro. Esta classe deve possuir os atributos titulo, autor, ano e editora. O atributo autor deve ser uma referência para uma instancia da classe Pessoa. De forma análoga, o atributo editora deve ser uma referência para uma instância da classe Editora.
#Crie a classe Emprestimo. Uma instância desta classe representa o empréstimo de uma obra (instância de Livro) realizada por um funcionário (instância da classe Pessoa) para um determinado usuário (instância da classe Pessoa) da biblioteca em uma determinada data.
#Crie um programa TestaEmprestimo. Este programa (classe) deverá, quando executado, efetuar o empréstimo de um livro para um determinado usuário. Não se esqueça de registrar, para a instância de Emprestimo a ser criada, o funcionário que efetuou o empréstimo. Este programa também deverá imprimir os detalhes do empréstimo criado.

#Classes
class Book:
    def __init__(self, title,author,year,publisher):
        self.title = title
        self.author = author
        self.year = year
        self.publisher = publisher

    def __str__(self):
        return f"'{self.title}' of {self.author}"

class Loan:
    def __init__(self,book,employee,user,date):
        self.book = book
        self.employee = employee
        self.user = user
        self.date = date

class TestLoan:
    def __init__(self,loan):
        self.loan = loan
    
    def testl(self,loan):
        print(f"The {self.loan.book} loaned to {self.loan.user} by {self.loan.employee} in {self.loan.date}.")

#Objects
white_nights = Book("White Nights","Fyodor Dostoyevsky",1848,"Penguin Classics")
loan_white_nights = Loan(white_nights,"Ronald","Nickolas","03/15/2026")

#Test
test = TestLoan(loan_white_nights)
test.testl(test)