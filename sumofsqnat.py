n=int(input("enter the number :"))

#n=1^2+2^2+....(n+1)^2

def sumOfSq(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+(i*i)
    return sum

print("Sum of Square of natural number is :",sumOfSq(n))


def sumOfCube(n):
    sum=0
    for j in range(1,n+1):
        sum=sum+(j*j*j)
    return sum
print("sumofcube is :", sumOfCube(n))