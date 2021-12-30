
n=int(input("Enter number :"))


if(n>1):
    for i in range(2,n):
        if(n%i==0):
            break
            print(f"{n} is not prime number")

    else:
        print(f"{n} is prime number")
