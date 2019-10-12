print("-------------------------------------------第一题-------------------------------------\n")
# 1. 求 1 ** 2 + 2 ** 2 + 3 ** 2 + ... + 9**2 的和

l1 = map(lambda x:x**2,range(1,10))

print("结果为：",sum(l1))


print("\n\n-------------------------------------------第二题-------------------------------------\n")
# 2. 求 1 ** 3 + 2 ** 3 + 3 ** 3 + ... + 9**3 的和
l2 = map(lambda x:x**3,range(1,10))
print("结果为：",sum(l2))


print("\n\n-------------------------------------------第三题-------------------------------------\n")
# 3. 求 1**9 + 2**8 + 3**7 + ... + 9**1的和  # 11377
l3 = map(pow,range(1,10),range(9,0,-1))
print("结果为：",sum(l3))


print("\n\n-------------------------------------------第四题-------------------------------------\n")
# 4. 将 1 ~20 内的偶数用filter筛选出来，形成列表
l4 = list(filter(lambda x : x%2==0,range(1,21)))
print("1~20内的偶数：",l4)


print("\n\n-------------------------------------------第五题-------------------------------------\n")
# 5. 用filter函数将1~100之间的所有素数(prime) 放入到列表中
def primenum(num):
	for x in range(2,(num//2)+1):
		if num % x == 0:
			return
	return num
	
l5 = list(filter(lambda x:x is not None,map(primenum,range(1,101))))
print("1~100以内的素数为：\n",l5)


print("\n\n-------------------------------------------第六题-------------------------------------\n")
# 6. names = ['Tom', 'Jerry', 'Spike', 'Tyke']
# 让names排序
#   排序的依据是字符串的反序
#          'moT'    'yrreJ'  'ekipS'  'keyT'
# L2 = sorted(names, ....) 
# 排序后:
# L2 = ['Spike', 'Tyke', 'Tom', 'Jerry']

l6_names = ['Tom', 'Jerry', 'Spike', 'Tyke']
l6 = sorted(l6_names,key=lambda s:s[::-1])
print("排序后：\n",l6)



print("\n\n-------------------------------------------第七题-------------------------------------\n")
# 7. 写函数input_student() 得到学生的姓名,成绩，年龄
# output_student(L) 打印学生信息
# (可以把以前的input_student/output_student函数直接拿过来用)
# 
# L = input_student()  # 输入一些学生信息
# print("按年龄从大到小排序后")
# L2 = sorted(L, .....)
# output_student(L2)
# print("按成绩从高到低排序后")
# L3 = sorted(L, .....)
# output_student(L3)
l7 = []

def input_student(*args):
	for index in range(0,len(args)):
		l7.append(args[index])


def output_student():
	# 对每个学生以年龄从大到小排序 
	l7.sort(key = lambda x:x[2],reverse = True)
	print("按照年龄从大到小排序：\n",l7)
	
	# 按照成绩从高到低排序
	l7.sort(key = lambda x:x[4],reverse = True)
	
	print("按照成绩从高到低排序：\n",l7)

# 输入学生的信息
input_student(['jiangyu','01',23,'男',100],['mly','02',22,'女',99],['zhangsan','03',17,'男',70],['lisi','04',18,'女',97])

output_student()


print("\n\n-------------------------------------------第八题-------------------------------------\n")
# 8.编写程序用递归求阶乘:
#   def myfac(x):
#       ....
# 
#   print(myfac(5))  # 120
#   print(myfac(4))  # 24

def factorial(n):
	
	if n == 1:
		return n
	
	return n*factorial(n-1)
	
s8 = int(input("请输入一个整数："))

print(factorial(s8))


print("\n\n-------------------------------------------第九题-------------------------------------\n")
# 9. 编写函数求阶乘 myfac(x), 用什么方法都可以
def myfac(x):
	for m in range(1,x):
		x *= m
	
	return x
	
s9 = int(input("请输入一个整数："))
print(myfac(s9))


print("\n\n-------------------------------------------第十题-------------------------------------\n")
# 10. 写程序算出1~20的阶乘的和
#   1!+2!+3!+.....+20!

def myfac10(n):
	if n == 1:
		return 1
	rs = myfac(n)
	return rs + myfac10(n-1)

s10 = int(input("请输入一个整数："))
print(myfac10(s10))



print("\n\n-------------------------------------------第十一题-------------------------------------\n")
# 11. 改写之前学生信息管理程序，添加如下四个功能
#   5)  按成绩从高至低打印学生信息
#   6)  按成绩从低至高打印学生信息
#   7)  按年龄从大到小打印学生信息
#   8)  按年龄从小到大打印学生信息
#   (要求原来输入的列表顺序保持不变)

# 真的不想重复练习了呀！！！！！
# 还是 sorted()函数呀！！！！


print("\n\n-------------------------------------------第十二题-------------------------------------\n")
# 12. 已知有列表:
#   L = [[3,5,8], 10, [[13, 14], 15, 18], 20]
#     1) 写一个函数print_list(lst) 打印出所有元素
#       print_list(L)  # 打印 ....
#     2) 写一个函数 sum_list(lst) 返回这个列表中所有元素的和
#  注:
#    type(x) 可以返回一个变量的类型
#    如:
#        type(20) is int        # 返回True
#        type([1,2,3]) is list  # 返回True

l12_1 = [[3,5,8], 10, [[13, 14], 15, 18], 20]
l12_2 = []

def myfun12(l):
	for index in range(0,len(l)):
		if type(l[index]) is list:
			myfun12(l[index])
		else:
			l12_2.append(l[index])

myfun12(l12_1)

print(l12_2)

print("和为：",sum(l12_2))
