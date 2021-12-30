# # start=int(input("Enter the starting number :"))
# # end=int(input("Enter the ending number :"))
# #
# # for i in range(start,end+1):
# #     if i>1:
# #         for j in range(2,i):
# #             if(i%j==0):
# #                 break
# #         else:
# #             print( i ,end=' ')
#
# def chatmsg(start):
#     final=""
#     for i in range(0,len(start)):
#         final=start[i]+final
#     return final
# st1="hello"
# st2=[]
# for i in range(len(st1)):
#     st2.append(st1[i])
# exc=st2
# print(chatmsg(exc))
#
# x=[1,"abcd",2,"efgh",[3,4]]
# y=x[0:50]
# z=y
# w=x
# x[1]=x[1]+'d'
# y[2]=4
#cd ..
# z[0]=0
# w[4][0]=1000


pairs=[(x,y) for x in range(9834,0,-8) for y in range(8624,0,-1) if(x+y)%3==0]
print(pairs)

