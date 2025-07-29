# ATW SIMULATOR
# t 1.if withdral amnt is greater than balance---)then show insufficient balance
# 2.if withdral amnt is less than balance--)
# if withdrawl amntJ is multiples of 100---)then writhdraul success
# else---withdrawl amnt should be multiples of 100 only

amount = int(input("enter the amount: "))
acc_bal = 20000
if amount > acc_bal:
    print("Insufficent balance ")
elif amount <= acc_bal:
    if(amount % 100 == 0):
        print("The withdrawl success")
        print("Remaining balance",acc_bal - amount)
    else:
        print("enter only hunderds ")



# if user knows-->F.E-->become-->F.DEV
# -->B.E-->become ->B.Dev
# -->D.B-->become ->D.dev
# -~>F.E AND B.E AND D.B-->F.S.DEV
# -->dont know anything-->go and learn skills

user_skills = input("Enter the user: ")
if user_skills == "frontend":
    print("your are a Frontend developer")
elif user_skills == "backend":
    print("Your a Backend developer")
elif user_skills == "database":
    print("your are a Database developer")
elif user_skills == "frontend,backend,database":
    print("your a full stack developer")
else:
    print("Not a developer")