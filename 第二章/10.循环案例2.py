"""
     案例2：猜数字游戏
      1.系统随机生成一个随机数
      2.用户根据提示猜数字，并将所猜数字存入系统
      3.如果猜错，系统提示猜大了或者猜小了，然后继续输入猜的数字
      4.如果猜对了，系统自动退出，游戏结束
"""
# count = 0
# import random
# random_num = random.randint(1,100)
# while True:  #这里代表进入了while死循环，因为没有在while后面加上循环截止的条件
#     if count >= 5:
#         print("您累计答错5次，停止答题！")
#         break
#     num = int(input("请输入数字（1~100）："))
#     if num<1 or num>100:
#         print("您输入的数字不符合要求！")  #无效输入不应该消耗次数
#         continue
#     else:
#         count += 1  #敲代码核心原则：DRY  不要重复你自己
#         if num > random_num:
#             print("您输入的数字太大了！再试试~")
#         elif num < random_num:
#             print("您输入的数字太小了！再试试~")
#         else:
#              print(f"猜对啦，恭喜您！您一共猜了{count}次")   #猜对了也要算上一次
#              break
# print(f"游戏结束，生成的随机数为{random_num}")



#练习1：将1~1000之间（含1000）所有5的倍数累加起来
# total = 0
# for i in range(1,1001):    #方式2：(5,1001,5)
#     if i % 5 == 0:           #total += i
#         total += i
#
# print(f"1~1000之间（含1000）所有5的倍数累加起来之和为{total}")

#练习2：统计字符串“akiwksjakdiklowiqaamnvbamvaxnsjdsjdsjkaaxkjd”中有多少个a和k
a_num = 0
k_num = 0
for i in "akiwksjakdiklowiqaamnvbamvaxnsjdsjdsjkaaxkjd":
    if i == "a":
        a_num += 1
    elif i == "k":
        k_num += 1
print(f"该字符串中有{a_num}个a,有{k_num}个k")
