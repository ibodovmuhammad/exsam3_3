######1########
# a = input().split()
# cnt=0
# for i in a :
#     cnt+=1
# print(cnt)
# _____________________________________________________________________

######2#####
# a = input().split()
# cnt=0
# for i in a :
#     d=0
#     for j in range(len(i)):
#         d+=1
#     if d>cnt:
#         cnt=d

# print (cnt)
# for i in a :
#     d1=0
#     for j in range(len(i)):
#         d1+=1
#     if d1==cnt:
#      print(i)
# __________________________________________________________________________________
#####3######
# list_num = input ().split()
# a = 999999
# for i in list_num:
#     if int(i)<a and int(i)%2!=0:
#         a=int(i)

# print(a)
#___________________________________________________________________________________
#####4#####
# num = list(map(int, input().split()))

# for i in range(len(num) - 1):
#     if num[i] * num[i + 1] > 0:
#         print(num[i], num[i + 1])
#         break
#_____________________________

####5#####
# num = list(map(int, input().split()))

# a = 1
# for i in range(1, len(num)):
#     if num[i] != num[i - 1]:
#        a += 1   

# print(a)
#___________________


####6#####
# list1=input().split()
# for i in list1:
#     cnt = 0
#     for j in list1:
#         if i==j:
#             cnt+=1
#     if cnt==1:
#         print(i, end=" ")
#_______________________________________________
#######7######
# list1=input().split()
# a=int(input())
# c=0
# for i in list1:
#     if c!=a:
#         print(i, end=" ")
#     c+=1

#_____________________________________________________

#####8########
# num = list(map(int, input().split()))

# a = 1
# for i in range(1, len(num)):
#     if num[i] != num[i - 1]:
#        a += 1   

# print(a)

#####9######
# li=input().split()
# a=int(input())
# cnt=1
# for i in li:
#     if a<=int(i):
#         cnt+=1

# print(cnt)


