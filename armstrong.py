#checking armstrong number
#floor division operator is “//”. It returns floor value for both integer and floating point

"""num=153
org=153
153>0 yes
sum=0+(153%10)*(153%10)*(153%10)
sum=0+3*3*3=27, num=153//10 num=15"""
import os

num=int(input("Enter the number :"))
org=num
sum=0
while(num>0):
    sum=sum+(num%10)*(num%10)*(num%10)
    num=num//10
if(org==sum):
    print(f"{org} is armstrong number")
else:
    print(f"{org} is not armstrong number")



#Python program to print Armstrong numbers within the given range in Python
lower=int(input("Enter the lower range :"))
upper=int(input("Enter the upper range :"))
for num in range(lower,upper+1):
    order = len(str(num))
    sum = 0  # find the sum of the cube of each digit
    temp = num
    while temp > 0:
        digit = temp % 10
        sum = sum+ digit ** order
        # temp= temp//10
        if num == sum:
            print(num, end=' ')

# lower = int(input("Enter lower range: "))
# upper = int(input("Enter upper range: "))
# for num in range(lower, upper + 1):
#     order = len(str(num))
#     sum = 0#find the sum of the cube of each digit
#     temp = num
#     while temp > 0:
#         digit = temp % 10
#         sum += digit ** order
#         temp //= 10
#         if num == sum:
#          print(num, end = ' ')