# s1 = "Hello"
# s2 = "Python"
# s3 = """加油
# 相信你"""
#
# print(s1)
# print(s2)
# print(s3)
#
# print(type(s1))
# print(type(s2))
# print(type(s3))
#
# msg = 'It\'s very good'
# print(msg)
# msg2 = "Hello的意思是'你好'"
# print(msg2)
# msg3 = "\t加油哦\n\t相信你"
# print(msg3)

name = "小熊"
age = 18
pro = "生物信息学"
hobby = "音乐"
print("大家好，我是" + name + ", 今年" + str(age) + "岁, 学习的专业是" + pro + ", 爱好" + hobby)

name = "小熊"
age = 18
pro = "生物信息学"
hobby = "音乐"
print("大家好，我是%s, 今年%s岁, 学习的专业是%s, 爱好%s" %(name, age, pro, hobby))

name = "小熊"
age = 18
pro = "生物信息学"
hobby = "音乐"
print(f"大家好，我是{name}, 今年{age}岁, 学习的专业是{pro}, 爱好{hobby}" )