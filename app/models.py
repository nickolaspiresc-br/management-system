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