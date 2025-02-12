class financialCalc:
    def __init__(self, p , r ,t, n=1):
        self.principal = p
        self.interest = r
        self.duration = t
        self.compounded = n

    def compound_interest(self):
        A = self.principal * ((1 + self.interest/self.compounded)**(self.duration * self.compounded))
        return round(A, 2)
    
    def simple_interest(self):
        A_S = self.principal * self.interest * self.duration
        return round(A_S, 2)

Person1 = financialCalc(1000, 0.1, 5)
Person1.compound_interest()
Person1.simple_interest()
print(f"The Amount after {Person1.duration} years with compound interest rate {Person1.interest*100}% is {Person1.compound_interest()}")
print(f"The Amount after {Person1.duration} years with simple interest rate {Person1.interest*100}% is {Person1.simple_interest()}")

