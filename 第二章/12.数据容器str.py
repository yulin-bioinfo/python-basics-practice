# s = "Hello-Python"
# # print(s[0:5:1])
# # print(s[0:5:])
# # print(s[:5:1])
# # print(s[8:6:-1]) #当步长为负数时，切片是是从右往左读取的，所以开始索引（较大的数）在右边，而结束索引在左边
# # print(s[4])
# a = s.find("Python")
# print(a)
# b = s.count("o")
# print(b)
# c = s.upper()
# print(c)
# d = s.lower()
# print(d)
# e = s.split("o")
# print(e)

# 案例：用户输入一个邮箱，要求判断该邮箱是否合法（一个@和至少一个.)
# mail = input("请输入您的邮箱：")
# if mail.count("@") == 1 and "." in mail:
# # 常规思路：if mail.count("@") == 1 and mail.count(".") >= 1:
#     print(f"{mail}是合法邮箱")
# else:
#     print(f"{mail}是非法邮箱")

# 作业1：判断输入的字符串是否为回文结构
# s = input("请输入一段字符串：")
# if s[::-1] == s:   #用切片反转，reverse是列表的方法
#     print(f"您输入的字符串为回文结构")
# else:
#     print(f"您输入的字符串不是回文结构！")

# 作业2：将用户输入的10个字符串，反转后全部大写，然后记录在列表中，再将列表遍历出来
result = []
for i in range(10):
    s = input(f"请输入第{i+1}个字符串：")
    result.append(s[::-1].upper())
for i in result:
    print(i)

