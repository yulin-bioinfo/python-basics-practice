"""
  案例1：根据输入的用户名和密码执行登陆操作，具体要求如下：
  1.正确的用户名和密码是xiaoming/123456  xiaozhang/666666
  2.输入用户名和密码进行登陆操作，知道登陆成功，程序结束运行;如果登陆失败，则继续输入用户名和密码进行登录
  3.输入的用户名和密码不能为空
  4.登陆成功，输出“登陆成功，进入B站首页~”
  5.登陆失败，输出“用户或密码错误，请重新输入”
  关键词： break ：只能够出现在循环中，表示结束/跳出循环
          contiune :只能够出现在循环中，表示中断本次循环，直接进入下一次循环
"""
i = 5  #只允许输错5次
while i > 0:  #如果写>=相当于给了6次机会
    username = input("请输入正确的用户名：")
    password = input("请输入正确的密码：")
    if username == ""  or password == "":
        print("输入的用户名或密码不能为空！请重新输入")
        i -= 1
        if i > 0:
            print(f"用户或密码错误，请重新输入,还剩{i}次机会")
        continue
    if username == "xiaoming" and password == "123456":
        print("登陆成功，进入B站首页~")
        break
    elif username == "xiaozhang" and password == "666666":
        print("登陆成功，进入B站首页~")
        break
    else:
        i -= 1
        if i > 0:
             print(f"用户或密码错误，请重新输入,还剩{i}次机会")
if i <= 0 :
    print("您已经累计输错五次，后续操作被禁止！")
