def out_line():
    # 注意有"()"，有":"，定义名字注意最好见名知义”
    print("____________")
    print("____________")


out_line()


# 函数的调用，上面这一个例子只是显示信息"___"，不做后续的处理，所以不用加return。如果涉及后续的计算和判断，那就需要加上return

def circle_area_c(r):
    area = round(3.14 * r * r, 1)
    c = 2 * 3.14 * r
    return area, c


# round可以选择保留几位小数
print(circle_area_c(3))
area, c = circle_area_c(3)
print(area)
print(c)


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

