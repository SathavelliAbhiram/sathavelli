num=int(input("enter any number"))
rev=0
rem=0
temp=num
while num>0:
    rem=num%10
    rev=rev*10+rem
    num=num//10
if temp==num:
    print(rev,"is number palindrome ")
else:
    print(rev,"is not number palindrome")
