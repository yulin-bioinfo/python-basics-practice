# if的条件判断：如果分数大于680，我就去清华上学
# score = float(input("请输入您的分数："))
# if score  > 680:
#     print("欢迎你来到清华读书\n也欢迎你开启精彩的大学生活")
# else:
#     print("分数未达标，可填报其他学校")
# print("-----------------")

# 补充知识点：
# / （正斜线）: 除法，是数学运算符（像一把刀) 也可以用于文件路径
# \ （反斜线）: 转义字符，本身不是运算符，改变的是后面字符的含义
# \n 换行  \t制表符  \"双引号


# 完成案例：B站登陆功能的实现 正确账号：123456  正确密码：666666
# true_account = "123456"
# true_password = "666666"
# account = input("请输入您的B站账号：")
# password = input("请输入您的B站密码：")
# if account == true_account and password == true_password:
#     print("登陆成功！\n欢迎进入B站~")
# # if account != true_account or password != true_password:
# #     print("登陆失败！\n账号或密码错误！")
# else:
#     print("登陆失败！\n账号或密码错误！")
#

# 案例：根据用户输入的年份，判断是闰年还是平年（非整百年能被4整除;整百年被400整除）
# year = int(input("请输入您要判定的年份："))
# if (year % 100 != 0 and year % 4 == 0) or year % 400 == 0:
#     print(f"{year}是闰年")
# else:
#     print(f"{year}是平年")

# 需求1：根据用户输入的数字，判断该数字是奇数还是偶数
# num = int(input("请输入您想判断的数字："))
# if num % 2 == 0:
#     print(f"您输入的数字{num}是偶数")
# else:
#     print(f"您输入的数字{num}是奇数")


# 需求2：根据用户输入的年龄，判断该用户是否已经成年
# age = int(input("请输入您的年龄："))
# if age >= 18:
#     print("您已经成年")
# else:
#     print("您未成年！")

# 需求3：根据用户输入的数字，判断该数为正数还是负数还是0
# num = float(input("请输入您想鉴别的数据："))
# if num > 0:
#      print(f"您输入的数字{num}为正数")
# elif num < 0:
#      print(f"您输入的数字{num}为负数")
# else:
#     print(f"您输入的数字{num}为0")

# # 需求4：根据用户输入的考试分数，判断该分数是否及格（大于等于60就是及格了）
# score = float(input("请输入您的分数："))
# if score >= 60:
#     print(f"您的分数为{score},已经及格")
# else:
#     print(f"您的分数为{score},未及格！")

# 根据输入用户名，密码进行登录系统  xiaozhang/111111   xiaowang/222222   xiaoming/333333
# username = input("请输入用户名：")
# password = input("请输入密码:")
# if username =="xiaozhang" and password =="111111":
#     print("登陆成功")
# elif username == "xiaowang" and password == "222222":
#     print("登陆成功")
# elif username == "xiaoming" and password == "333333":
#     print("登陆成功")
# else:
#     print("登陆失败，账号或密码错误")
# 补充知识点：elif可以一直加


# 需求1：输入考试成绩，判断等级
# score = float(input("请输入您的考试成绩："))
# if score >= 85:
#     print(f"您的分数为{score}，等级为优秀")
# elif 60 <= score < 85:
#     print(f"您的分数为{score}，等级为及格")
# else:
#     print(f"您的分数为{score}，等级为不及格")

# 需求2：购物折扣计算：根据输入的购物车的商品金额，进行优惠并且计算出实付金额
# money = float(input("请输入商品金额："))
# if money >=500:
#     print(f"商品金额为{money}，已享受到八折优惠，实付金额为{money * 0.5}")
# elif 300 <= money < 500:
#     print(f"商品金额为{money},已享受到九折优惠，实付金额为{money * 0.9}")
# elif 100 <= money < 300:
#     print(f"商品金额为{money},已享受到九五折优惠，实付金额为{money * 0.95}")
# else:
#     print(f"商品金额为{money}，未享受到优惠，实付金额为{money}")

# 案例：输入三条边长，判断三角形类型
# 补充：pass表示空语句，语法占位作用；if里面还可以嵌套if
# a = int(input("请输入第二条边长:"))
# c = int(input("请输入第三条边长:"))
# if a + b > c and b + c > a and c + a > b:
#     if a==b==c:
#         print(f"您输入的三条边{a},{b},{c}构成等边三角形")
#     elif a ==b or b == c  or c == a :
#         print(f"您输入的三条边{a},{b},{c}构成等腰三角形")
#     else:
#         print(f"您输入的三条边{a},{b},{c}构成普通三角形")
#
# else:
#     print(f"您输入的三条边{a},{b},{c}不构成三角形")


# 根据用电量，算电费
degree = float(input("请输入用户的用电度数:"))
if degree >4800:
    print(f"您的用电度数为{degree},电费单价为0.7883元/度，电费为{degree * 0.7883}")
elif 2880<=degree<=4800:
    print(f"您的用电度数为{degree},电费单价为0.5383元/度，电费为{degree * 0.5383}")
else:
    print(f"您的用电度数为{degree},电费单价为0.4883元/度，电费为{degree * 0.4883}")
