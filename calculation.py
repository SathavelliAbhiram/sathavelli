print("\n 1.Addition \n 2.Substraction \n 3.multiplication \n 4.divison \n 5.reaminder \n 6.power")
choice=input("enter any option")
a=int(input("enter a value"))
b=int(input("enter b value"))
if(choice=='1'):
    print(a+b)
    print("\n addition")
elif(choice=='2'):
    print(a-b)
    print("\n substraction")
elif(choice=='3'):
    print(a*b)
    print("\n multipilaction")
elif(choice=='4'):
    print(b/a)
    print("\n divison")
elif(choice=='5'):
    print(a%b)
    print("\n remainder")
elif(choice=='6'):
    print(a**b)
    print("exponential")
else:
    print("wrong input")


