# s1 = {1,2,4,5,9,10,27,8,29}
# # print(s1)
# # print(type(s1))
# # s2 = set()
# # print(s2)
# # print(type(s2))
# # s1.add(900)
# # print(s1)
# # s1.remove(2)
# # print(s1)
# # s1.pop()
# # print(s1)
# # s1.clear()
# # print(s1)
# s2 = {3,45,88,91,56,62,90,78,1,2,3}
# print(s2.difference(s1))
# print(s2.union(s1))
# print(s2.intersection(s1))

# 案例
football_set = {"王林", "曾牛", "徐立国", "遁天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}
# 选修篮球学生名单
basketball_set = {"张铁", "墨居仁","王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}
# 选修法语学生名单
french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子",  "红蝶", "厉飞雨", "韩立", "曾牛"}
# 选修艺术学生名单
art_set = { "遁天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}
# 1. 找出同时选修了 法语 和 艺术 的学生
# fa_set = french_set.intersection(art_set)
# print(fa_set)
fa_set = french_set & art_set
print(f"同时选修了 法语 和 艺术 的学生{fa_set}")
# 2. 找出同时选修了所有四门课程的学生
all_set = football_set & basketball_set & french_set & art_set
print(all_set)
# 3. 找出选修了足球, 但是没有选修篮球的学生 - 差集
fnb_set1 = football_set.difference(basketball_set)
print(f"选修了足球, 但是没有选修篮球的学生{fnb_set1}")
fnb_set2 = football_set - basketball_set
print(f"选修了足球, 但是没有选修篮球的学生{fnb_set2}")
fnb_set3 = {s for s in football_set if s not in basketball_set}
print(f"选修了足球, 但是没有选修篮球的学生{fnb_set3}")
# 4.获取每个同学选修课的数量     #这一步是重点！！！！！
all_set = football_set | basketball_set | french_set | art_set
all_list = [*football_set,*basketball_set,*french_set,*art_set]
for s in all_set:
    print(f"{s}选修了{all_list.count(s)}门选修课程")