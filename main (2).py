# Python program to create Bankaccount
# with both a deposit() and a withdraw() function 
class Bank_Account:
    def _init_(self):
     self.balance=0         
     print("Hello!!! Welcome to the Deposit & Withdrawal Machine")
  
def deposit(self):
   amount=float(input("Enter amount to be Deposited: "))
   self.balance =0 
   print("\n Amount    Deposited:",amount)

   def withdraw(self):
     amount = float(input("Enter amount to be withdrawn:"))
                          
     if self.balance>=amount:    
       self.balance-=amount
       print("\n You Withdrew:",            amount) 
     else: 
       print("\n Insufficient balance ")

   def display(self):
     print("\n Net Available Balance=",self.balance)
# Driver code
# creating an object of class s = Bank Account()
# Calling functions with that class object  
s.deposit()
s.withdraw()
     s.display()