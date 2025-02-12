class financialCalc:
    def __init__(self, p , r ,t, n=1):
        self.principal = p
        self.interest = r
        self.duration = t
        self.compounded = n

    def compound_interest(self):
        A = self.principal * ((1 + self.interest/self.compounded)**(self.duration * self.compounded))
        return round(A, 2)
        

Person1 = financialCalc(1000, 0.1, 5)
Person1.compound_interest()
print(f"The Amount after {Person1.duration} years with interest rate {Person1.interest*100}% is {Person1.compound_interest()}")