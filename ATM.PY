balance=10000
pin=801991
cnt=0
flag=0

while True:
    yourpin=int(input("enter your pin"))

    if pin==yourpin:
        print("login succesfully")
        flag=True
        break
    elif pin!=yourpin:
        print("enter pin correctly")
        cnt=cnt+1
        if cnt==3:
            print("your chances are over")
            flag=False
            break        
while flag:
    print("1.check balance \n 2.Deposit your  cash \n 3.withdraw your cash  \n 5.Exit")
    ch=int(input("enter your choice"))
    if ch==1:
        print("your balance is ",balance)
    elif ch==2:
        deposit=int(input("enter your deposite ammount"))
        balance=balance+deposit
        print("your balance after deposit",balance)
    elif ch==3:
        withdraw=int(input("enter your with draw your amount"))
        if balance>=withdraw:
            print("\n your cash is sufficient ")
            print("take your cash",withdraw)
            balance=balance-withdraw
            print("your balance after with draw",balance)
        else:
            print("your cash in sufficent")
            print("your balance is ",balance)
    elif ch==4:
        break
print("1.Excelent \n 2.Good \n 3.Average \n 4.Bad")
feedback=input(" how our bank services are give your opinion ")    
if feedback=='1':
    print("THANKYOU")
elif feedback=='2':
    print("THANKYOU")
elif feedback=='3':
    review=input("if any improvement can take ")
    print("THANKYOU")
else:
    review=input("if any improvement can take")
    print("THANKYOU")
print("VISIT AGAIN")
    
                   
