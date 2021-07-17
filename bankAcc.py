class BankAccount:
    def __init__(self,accHolder,bal):
        self.accHolder=accHolder
        self.bal=bal
    def deposit(self,amt):
        self.bal=self.bal+amt
        print("Your available balance is " +str(self.bal))
    def withdrawal(self,amt):
        if(amt>self.bal):
            print("Insufficient balance")
        else:
            self.bal=self.bal-amt
            print("Your available balance is " +str(self.bal))

   
a=BankAccount("Neeraj",5000)
print(a)
print(a.accHolder)
print(a.bal)
a.withdrawal(3500)
a.deposit(2000)
a.withdrawal(1000)
a.deposit(2000)
a.withdrawal(2500)