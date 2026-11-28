# 案例1：定义一个函数，根据传入的底和高来计算三角形的面积
def triangle_area(b, h):
    """根据输入的三角形的底和高来计算三角形的面积
   :param b:三角形的底长
    :param h:三角形的高
    """
    return b * h / 2


b = float(input("请输入三角形的底长:"))
h = float(input("请输入三角形的高:"))
print(f"三角形的面积为：{triangle_area(b, h)}")


# 案例2：定义一个函数用来求字符串中的元音字母个数
def count_aeiou(s):
    num = 0
    for i in s:
        if i in "aeiouAEIOU":
            num += 1
    return num


s = input("请输入您想查询的字符串:")
print(f"您输入的字符串{s}中元音字母个数为{count_aeiou(s)}")


# 案例3：定义一个函数，计算班级分数得最高分，最低分，平均分
def calc_score(score_list):
    max_s = max(score_list)
    min_s = min(score_list)
    avg_s = round(sum(score_list) / len(score_list), 1)
    # 这里的round表示保留一位小数
    return max_s, min_s, avg_s


score_list = [651, 705, 564, 431]
print(calc_score(score_list))


# 作业1：定义一个函数，根据输入的分数判断对应的等级并返回  A:≥90  B：≥75  C：≥60  D：＜60
def evaluate_score(score):
    if score >= 90:
        return "该学生等级为A"
    elif 75 <= score < 90:
        return "该学生等级为B"
    elif 60 <= score < 75:
        return "该学生等级为C"
    elif score < 60:
        return "该学生等级为D"


score = float(input("请输入分数"))
print(f"该学生分数为{score},等级为{evaluate_score(score)}")


# 作业2：定义一个函数，判断该字符串是不是回文，并返回bool值
def judge_huiwen(s):
    if s == s[::-1]:
        # 这是字符串判断回文的方法，列表才有reverse这个功能
        return True
    else:
        return False


s = input("请输入您想判断的字符串：")
print(f"判断该字符串是否为回文的结果为：{judge_huiwen(s)}")


# 作业3：定义一个函数，实现时间转换功能，将传入的秒转换成小时、分钟、秒
def transform_second(s):
    hour = s // 3600  # 这个表示整除
    minute = (s % 3600) // 60
    second = s % 60
    return hour, minute, second


s = int(input("请输入想要转换的秒:"))
print(transform_second(s))


# 作业4：根据输入的三角形的边长，判断三角形的类型（等边，等腰，普通，或者不能构成三角形）
def judge_triangle(s1, s2, s3):
    max_side = max(s1, s2, s3)
    if s1 + s2 + s3 - max_side > max_side:
        if s1 == s2 == s3:
            return "该三角形为等边三角形"
        elif s1 == s2 or s1 == s3 or s2 == s3:
            return "该三角形为等腰三角形"
        else:
            return "该三角形为普通三角形"

    else:
        return "不能构成三角形"


# return后面要加一个空格
s1 = float(input("请输入三角形的第一个边长"))
s2 = float(input("请输入三角形的第二个边长"))
s3 = float(input("请输入三角形的第三个边长"))
print(f"根据您输入的三条边长{s1},{s2},{s3},该三角形为{judge_triangle(s1, s2, s3)}")