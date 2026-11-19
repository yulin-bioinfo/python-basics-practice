# t = (1,2,3,4,5,6,7,8,9)
# print(t)
# print(type(t))
# print(t[1])
# print(t.count(2))
# print(t.index(2))
# print(t[::2])
#如果元组中只有一个元素，要在元素后面加上逗号，比如t(100,)


# t1 = (1, 2, 3, 4)
# a, b, c, d = t1
# print(a, b, c, d)
# a, *b, c = t1
# print(a)
# print(*b)
# print(c)

# 案例1：a = 10  b = 20  将a和b的值互换
# a = 10
# b = 20
# a, b = b, a
# print(a, b)
# 以上是简化过程，下面展示完整过程
# t = (a, b)  #这里也可以不用加括号，等号右边如果用逗号隔开多个值，python会自动打包成元组
# b, a = t
# print(a, b)
# 案例2：a = 100,b = 200, c = 300  将a,b,c分别赋值给c,a,b
# a = 100
# b = 200
# c = 300
# c, a, b = a, b, c
# print(a, b, c)

# 案例：
# s1 小明 99 101 89
# s2 小红 90 123 58
# s3 小张 88 119 134
# 1.计算每位同学的总分和各科平均分

s = (
    ("s1", "小明", 99, 101, 89),
    ("s2", "小红", 90, 123, 58),
    ("s3", "小张", 88, 119, 134),
)

for i in s:
    id = s[0]
    name = s[1]
    chinese = s[2]
    math = s[3]
    english = s[4]
    total = chinese + math + english
    avg = total / 3
    print(f"{id},{name},{chinese},{math},{english},{total},{avg}")

# 2.统计各科成绩的最高分最低分
chinese_score = [s[2] for i in s]
print(f"语文最高分为：{max(s[2])}")
