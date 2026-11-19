# day = input("请输入星期几（1——7）：")
# match day:
#     case "1":
#         print("今天是周一，开会日")
#     case "2":
#         print("今天是周二，培训日")
#     case "3":
#         print("今天是周三，实习日")
#     case "4":
#         print("今天是周四，规划日")
#     case "5":
#         print("今天是周五，总结日")
#     case "6" | "7":
#         print("周末啦，休息！")
#     case _:         #用于匹配其他的所有情况
#         print("输入错误")


# 实现简易计算机的功能，用户输入两个数，进行 + - * / 运算
# num1 = float(input("请输入第一个数据："))
# num2 = float(input("请输入第二个数据:"))
# oper = input("请输入您想进行的运算(+ - * /):")
#
# match oper:
#     case "+":
#         print(f"{num1} + {num2} = {num1 + num2}")
#     case "-":
#         print(f"{num1} - {num2} = {num1 - num2}")
#     case"*":
#         print(f"{num1} * {num2} = {num1 * num2}")
#     case"/" if num2 != 0 :    #if条件成立才会匹配此结果
#         print(f"{num1} / {num2} = {num1 / num2}")
#     case _:
#         print("该操作不符合条件！")

#编写一个游戏角色控制中心，根据玩家的不同指令，控制游戏角色执行相应动作
# oper = input("请输入您想进行的操作：")
# match oper:
#     case "上"|"w"|"W":
#         print("角色向上移动")
#     case "下"|"s"|"S":
#         print("角色向下移动")
#     case "左"|"a"|"A":
#         print("角色向左移动")
#     case "右"|"d"|"D":
#         print("角色向右移动")
#     case "跳"|" ":
#         print("角色跳跃")
#     case "攻击"|"j"|"J":
#         print("角色发动攻击")
#     case "退出"|"esc"|"ESC":
#         print("角色退出游戏")
#     case _:
#         print("您输入的指令错误！")


