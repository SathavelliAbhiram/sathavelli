n1=15
n2=10
n3=25

if (n1>n2  and n1<n3) or (n1 > n3 and n1<n2):
    print(n1,"is big")
elif(n2>n1 and n2<n3) or (n2 > n3 and n2 < n1):
    print(n2,"is big ")
else:
    print(n3,"is big")
