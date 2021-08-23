"""
The objective here is to create two classes 'Borrower' and 'Loan'
and to create functions to verify rules to approve or deny a loan for a borrower
"""

"""
1
if
    the credit score of 'the borrower' is less than 200
then
    add "Credit score below 200" to the messages of 'the loan' ;
    reject 'the loan' ;
"""

#The line "def ruleX(...):" is part of the prompt
def rule1(borrower, loan):
    if borrower.credit_score < 200:
        loan.messages.append("Credit score below 200")
        loan.reject()

"""
2
if
    the yearly repayment of 'the loan' is more than the yearly income of 'the borrower' * 0.3
then
    add "Too big Debt-To-Income ratio" to the messages of 'the loan' ;
    reject 'the loan' ;
"""

def rule2(borrower, loan):
    if loan.yearly_repayment > borrower.yearly_income * 0.3:
        loan.messages.append("Too big Debt-To-Income ratio")
        loan.reject()

"""
3
if
    the yearly income of 'the borrower' is more than 0
    and all of the following conditions are true:
        - the yearly repayment of the loan * 100 / the yearly income of the borrower is at least 0 and less than 30
        - the credit score of the borrower is at least 0 and less than 200
then 
    add "debt to income too high compared to credit score" to messages of the loan 
    reject 'the loan'
"""

def rule3(borrower, loan):
    if borrower.yearly_income > 0 and loan.yearly_repayment * 100 / borrower.yearly_income >= 0 and loan.yearly_repayment * 100 / borrower.yearly_income < 30 and borrower.credit_score >= 0 and borrower.credit_score < 200:
        loan.messages.append("debt to income too high compared to credit score")
        loan.reject()

"""
4
if
    the amount of 'the loan' is more than 1000000
then
    add "The loan cannot exceed 1,000,000" to the messages of 'the loan' ;
    reject 'the loan' ;
"""

def rule4(borrower, loan):
    if loan.amount > 1000000:
        loan.messages.append("The loan cannot exceed 1,000,000")
        loan.reject()

"""
Create two classes: 'Borrower' and 'Loan' corresponding to the defined rules
"""

    
class Borrower:
    def __init__(self, credit_score, yearly_income):
        self.credit_score = credit_score
        self.yearly_income = yearly_income

class Loan:
    def __init__(self, amount, yearly_repayment):
        self.amount = amount
        self.yearly_repayment = yearly_repayment
        self.messages = []
        self.approved = False

    def reject(self):
        self.approved = False

    def approve(self):
        self.approved = True