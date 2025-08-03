
class parent:
    def pmethod(self):
        print("i am method from parent")
    def pmethod2(self):
        print("i am method2 form parent")
class child(parent):
    def cmethod(self):
        super().pmethod2()
        print("I AM METHOD FROM CHILD")
    def cmethod2(self):
        super().pmethod()
        print("i am calss form the method cmethod")

obj = child()
obj.pmethod()
child.cmethod2(obj)
child.cmethod2(obj)
obj.cmethod2()

class application:
    def __init__(self,name,color,categotry):
        self.name = name
        self.logo_color = color
        self.category = categotry
    def getappinfo(self):
        print(f"{self.name},{self.logo_color},{self.category}")
instagram = application("instagram","pink","social media")
instagram.getappinfo()
facebook = application("facebook","blue","social media")
zomato = application("zomata","red","food")
print(facebook.name)
application.getappinfo(instagram)



class BankAccount:
    def __init__(acut,name,ifsc,acut_num,branch,balance):
        acut.name = name
        acut.ifsc = ifsc
        acut.acut_num = acut_num
        acut.branch = branch
        acut.balance = balance
    def deposit(acut,amount):
        acut.balance+= amount
    def withdrawl(acut,amount):
        acut.balance-= amount
    def checkbalnce(acut):
        print(f"{acut.balance}")
hari_acut = BankAccount("hari","SAIU1242",839647563,"kphb",10000)
hari_acut.checkbalnce()
hari_acut.deposit(5000)
hari_acut.checkbalnce
hari_acut.withdrawl(2000)
hari_acut.checkbalnce()




# Create a class called SavingsAccount that inherits from the BankAccount class. Add a new method called add_interest() which adds 5% interest to the current balance.
# Requirements:
# SavingsAccount should inherit from BankAccount.
# The method add_interest() should calculate and add 5% of the current balance to it.
# Create an object of SavingsAccount, deposit money, add interest, and display final balance.

    
class BankAccount:
    def __init__(self,holder_name,acc_num,ifsc,branch,balance):
        self.holder_name = holder_name
        self.acc_num = acc_num
        self.ifsc = ifsc
        self.branch  = branch
        self.balance = balance
    def add_interest(self,intrest):
        intrest = 0.05*self.balance
        self.balance+=intrest
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        self.balance-=amount
    def checkbalance(self):
        print(f"{self.balance}")

Savingsaccount = BankAccount("hari",234343443,"sbi008","kphb",10000)
Savingsaccount.add_interest(150000)
Savingsaccount.checkbalance()
Savingsaccount.withdraw(5000)
Savingsaccount.checkbalance()