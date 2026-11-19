#列表list切片
# 1.定义列表
s = ["A","B","C","D","E","F","G","H","I"]
# 2.切片操作  s[开始索引：结束索引：步长]
# print(s[0:5:1])
# print(s[0:5:2])
# print(s[0:-2:2])
# print(s[::2])
# print(s[::-1])
# print(s[3::])
#3.列表的常见方法 append insert remove pop sort reverse
# s.append(100)
# print(s)
# s.insert(0,1)
# print(s)
# s.remove(1)
# print(s)
# s.pop(4)
# print(s)
# s.reverse()
# print(s)
# s.pop()
# print(s)
# 案例1：用户输入十个数字，要求进行排序，并且求出最大值，最小值和平均值
# num_list = []
# for i in range(10):
#     num = int(input("请输入1个有效数字："))  #必须写变量接收数据
#     num_list.append(num)
# print("列表为：",num_list)
# num_list.sort()
# print("排序后列表为：",num_list)
# print("列表中的最大值为:",num_list[-1]) #写成-1更好，写9的前提是用户输入的刚好是10个数字，如果用户输入不足10个就会越界
# print("列表中的最小值为:",num_list[0])
# print("列表中的数据平均值为:",sum(num_list)/len(num_list))
# # sum() 表示求和，len() 表示列表的长度或者说数据的个数

#案例2：合并两个列表中的元素，并对合并后的结果进行去重处理（去除列表中的重复元素）
# num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
# num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]
# for i in num_list1:
#     num_list2.append(i)
#
# print("合并以后的列表为：",num_list2)
 #方法2解包操作：（将列表这一容器解包成一个个的独立元素）  组包
#      num_list = [*num_list1, *num_list2]
#方法3：num_list = [num_list1 + num_list2]
# new_list = []
# for i in num_list:
#     if i not in new_list:
#         new_list.append(i)
#
# print("去重以后的列表",new_list)

#案例3：生成1到20的平方列表
# 方式1：传统方法
# num_list = []
# for i in range(1,21):
#     num_list.append(i**2)
# print("生成的列表为：",num_list)
# #方式2：列表推导式（按照一定的规则快速生成一个列表，语法格式：[要输入的值 for i in 列表/序列]
# num_list2 = [i**2 for i in range(1,21)]
# print("生成的列表为：",num_list2)


# 案例4：从一个数字列表中抽出偶数，并计算其平方，组成新的列表
# num_list = [22, 43, 85, 33, 45, 67, 93, 30,42]
# new_list = [i**2 for i in num_list if i % 2 == 0]
# print("新的列表为：", new_list)

#作业1：将下列列表合并为一个新的列表，并去掉重复元素，排好序后（升序）后输出到控制台
# list1 = ["M", "A", "C", "E", "F", "G", "H", "L", "N", "I", "J", "K", "O"]
# list2 = ["x", "Z","T","Y", "D", "E", "F", "G"]
# list3 = ["W", "A", "S", "D"]
# list4 = list1 + list2 + list3 #(这里不用括号再括起来了，不然会让上面三个列表变成新列表的元素)
# new_list = []
# for i in list4:
#     if i not in new_list:
#         new_list.append(i)
# new_list.sort()
# print("排序后：",new_list)
#变式题目：
a = [1,2,3,4,5]
b = [2,3,4,5,6]
c = [3,4,5,6,7]
# result = []
# for i in a:
#     if i in b and i in c:
#         result.append(i)
# print(result)
# 变式题目2：
# new_list = a + b + c
# result = []
# for i in new_list:
#     if i in (a or b ) and i not in c:
#         if i not in result:
#               result.append(i)
# print("结果为：",result)
#作业2：将下列列表中能被3或5整除的数字提出来，并将它们平方获得新的列表
list = [22,44,56,78,37,42,72,98,27,86,105,981]
new_list = []
for i in list:
    if i % 3 ==0 or i % 5 == 0:
        new_list.append(i**2)
print(new_list)