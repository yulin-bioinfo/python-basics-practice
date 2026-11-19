# msg = input("请输入需要遍历的字符串：")
# for i in msg:
#     print(f"您遍历的元素为：{i}")
# else:
#     print("遍历结束")

# 计算1——100所有奇数之和
# 原始版本
# total = 0
# for i in range(1,101):
#     if i % 2 == 0 :
#         total += i
# print(f"1——100所有奇数之和为{total}")
# 简化后
# total = 0
# for i in range(1,101,2):   #一定要加上range
#     total += i
# print(f"1——100所有奇数之和为{total}")



# i = 1
# total = 0
# while i <101:
#     if i % 2 == 1:
#         total += i
#     i += 1
# print(f"1——100所有奇数之和为{total}")

# # 计算100——500所有3的倍数之和
# total = 0
# for i in range(100,501):
#     if i % 3 == 0:
#         total += i
# print(f"100——500所有3的倍数之和为{total}")


"""
案例：输入一个长为10，宽为5的长方形
print("*"):自带换行效果，每次执行都会输入到新的一行中
print("*", end="") end表示每次输出以什么结束，默认为 \n ,表示换行
"""
# 三个冒号表示注释
# m = int(input("请输入长方形的长度："))
# n = int(input("请输入长方形的宽度："))
# for i in range(n):
#     for j in range(m):
#         print("*",end = " ")
#     print()   #里面是空的，这就表示默认的换行符

# 案例：制作99乘法表
# for i in range(1,10):
#     for j in range(1,i+1):    #range(a,b)中范围是不包括b的！
#         print(f"{j}*{i}={i*j}",end = "  ")
#     print()

#练习1：根据输入的直角边的边长，打印等腰直角三角形
# s = int(input("请输入直角边的边长："))
# for i in range(1,s+1):
#     for j in range(1,i+1):
#         print("*",end = " ")
#     print()

# 打印数字金字塔
# s = int(input("请输入您想创建的数字金字塔（输入数字就行）："))
# for i in range(1, s+1):
#     # print("  "*(s - i),end="")  （居中金字塔写法）
#     for j in range(1,i+1):
#         print(j,end= " ")
#     print()


# 打印国际象棋棋盘  ✨✨
# c = int(input("请输入您想创建的棋盘的长："))
# k = int(input("请输入您想创建的棋盘的宽："))
# for i in range(1,k+1):
#     for j in range(1,c+1):
#         if (i + j )%2==1:
#             print("黑",end = " ")
#         else:
#             print("白",end = " ")
#     print()
