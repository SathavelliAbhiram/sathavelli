num=int(input("enter anynumber"))
rem=0
sum=0
while num>0:
    rem=num%10
    sum=sum+rem
    num=num//10
    if sum>9:
        num=sum
    else:
        print(sum)
        break
    

    

