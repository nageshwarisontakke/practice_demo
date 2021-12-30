#stroe in list
nterm=int(input("Enter number :"))

n1,n2=0,1
count=0

if (nterm<0):
    print("enter the positive number")
elif(nterm==1 or nterm==0):
    print("fibonacii series is ",nterm,":")
    print(n1)
else:
    print("Fibonacci series is :")

    while(count<nterm):
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count=count+1
if(nth==nterm):
    print("is fibonacci")
else:
    print("is not fibonacci")
