def circle_area(r):
    area = 3.14 * r ** 2
    return area


area = circle_area(10)
print(area)


def rectangle_area(l, w):
    """
    该函数用于已知长方形的长和宽来求长方形的面积
    :param l :长方形的长
    :param w :长方形的宽
    :return :返回值为长方形的面积

    """
    area = l * w
    return area


print(rectangle_area(10, 2))
help(rectangle_area)  # 函数的说明文档


# 函数的嵌套调用
def function_a():
    print("a...before")
    function_b()
    print("a...after")


def function_b():
    print("b...before")
    function_c()
    print("b...after")


def function_c():
    print("c...")


function_a()
print("函数调用完毕～")