print("-------------------------------------------第一题-------------------------------------\n")
# 1. 写一个函数 mymax, 实现返回两个数的最大值:
#    如:
#       def mymax(a, b):
#          ... 此处自己填写
#       print(mymax(100, 200))  # 200
#       print(mymax(50, 10))    # 50
#       print(mymax('ABC', 'ABCD')) # ABCD

def mymax(a,b):
	l = [a,b]
	return max(l)

s1_1 = int(input("请输入第一个数："))
s1_2 = int(input("请输入第二个数："))

print("最大的数为：",mymax(s1_1,s1_2))



print("\n\n-------------------------------------------第二题-------------------------------------\n")
# 2. 写一个函数 input_number
#     def input_number():
#         ....
#     此函数用来获取用户循环输入的整数，当用户输入负数时结束输入
#     将用户输入数以列表的形式返回，再用内建函数max, min, sum 示出用户输入的最大值，最小值及和:
#     如:
#       L = input_number()
#       print(L)  # 打印此列表
#       print("用户输入的最大数是:", max(L))
#       print("用户输入的最小数是:", min(L))
#       print("用户输入的和是:", sum(L))
def input_number():
	l2 = []
	while True:
		s2 = int(input("请您输入整数："))
		if s2 < 0:
			return l2
		else:
			l2.append(s2)

l2_1 = input_number()
print(l2_1)
print("您输入的最大数是：",max(l2_1))
print("您输入的最小数是：",min(l2_1))
print("您输入的和是：",sum(l2_1))



print("\n\n-------------------------------------------第三题-------------------------------------\n")
# 3. 写一个函数sum3(a, b, c):
#    用于返回三个数的和
#    写一个函数pow3(x) 用于返回x的三次方(立方)
# 
#    1) 用以上函数计算
#       1**3 + 2 ** 3 + 3**3的和
#    2)  计算 1 + 2 + 3 的和的立方
#        即(1+2+3)**3

def sum3(a,b,c):
	return a+b+c


def pow3(x):
	return x**3

s3_a = int(input("请输入第一个整数："))
s3_b = int(input("请输入第二个整数："))
s3_c = int(input("请输入第四个整数："))
print("三个数的和为：",sum3(s3_a,s3_b,s3_c),end="\n\n")

s3_x = int(input("请输入一个整数："))
print("该数的三次方为：",pow3(s3_x))


print("\n\n-------------------------------------------第四题-------------------------------------\n")
# 4. 写一个函数 mysum(), 可以传入两个实参或三个实参.
#    1) 如果传入两个实参，则返回两个实参的和
#    2) 如果传入三个实参，则返回前两个实参的和对第三个实参求余的结果
# 
#   print(mysum(1, 100))    # 101
#   print(mysum(2, 10, 7))  # 5 返回:(2+10) % 5

print(r'''请输入参数:
	若想输入两个参数(如输入1,2)：12
	若想输入三个参数(如输入1,2,3)：123
	  ''')

s4_1 = input()
def mysum(*args):
	print("您输入的参数是：",args)
	if len(args) == 2:
		print("结果为：",(int(args[0])+int(args[1])))
	elif len(args) ==3:
		print("结果为：",((int(args[0])+int(args[1]))%int(args[2])))
	else:
		print("您输入的参数不规范，要求2或3个参数！")

mysum(*s4_1)

print("\n\n-------------------------------------------第五题-------------------------------------\n")
# 5. 写一个函数，mysum , 可以传入任意个实参的数字，返回所有实参的和
#   def mysum(.....):
#       ......
#   print(mysum(1, 2, 3, 4))  # 10
#   print(mysum(2,4,6))  # 12

def mysum5(*args):
	return sum(args)

print(mysum5(1,2,3,4))


print("\n\n-------------------------------------------第六题-------------------------------------\n")
# 6. 写一个myrange函数，此函数返回一个符合range规则的整数列表
# 如:
#   L = myrange(3)
#   print(L)  # [0,1,2]
#   L = myrange(3, 6)
#   print(L)  # [3, 4, 5]
#   L = myrange(1, 10, 3)
#   print(L)  # [1, 4, 7]

def myrange(*args):
	l6_1 = []
	if len(args) == 1:
		l6_1 = list(range(0,args[0]))
	elif len(args) == 2:
		l6_1 = list(range(args[0],args[1]))
	elif len(args) == 3:
		l6_1 = list(range(args[0],args[1],args[2]))
	
	return l6_1
	
print(myrange(3))
print(myrange(3,6))
print(myrange(1,10,3))


print("\n\n-------------------------------------------第七题------------------------------------\n")
# 7. 素数prime函数练习
# 1)  写一个函数isprime(x)  判断x是否为素数，如果是素数，返回True,否则返回False
# 2) 写一个函数prime_m2n(m, n), 返回从m开始到n结束(不包含n)的范围内的素数列表
#   如:
#     L = prime_m2n(1, 10)
#     print(L) # [2,3,5,7]
# 3) 写一个函数primes(n), 返回指定范围内素数(不包含n)的全部素数的列表,并打印这些素数
#   如:
#     L = prime(20)
#     print(L)  # [2,3,5,7,11,13,17,19]
#   1) 打印 100以内的全部素数
#   2) 打印 100以内全部素数的和

def prime(x):
	for i in range(2,x//2+1):
		if x % i == 0:
			return -1
	
	return 0
	
def prime_m2n(a,b):
	l7 = []
	for x in range(a,b):
		if prime(x) == 0:
			l7.append(x)
	
	return l7

def primes(n):
	return prime_m2n(0,n)
		
print("测试1：")
s7 = int(input("请输入一个数："))
if prime(s7) == -1:
	print("该数不是素数！")
else:
	print("该数是素数！")


print("测试2：",prime_m2n(1,10))
print("测试3：",primes(20))


print("\n\n-------------------------------------------第八题------------------------------------\n")
# 8. 修改之前的学生信息管理程序:
#   编写两个函数用于封装 录入学生信息　和　打印学生信 息的功能
#     1) 
#     def input_student():
#     　　　　#此函数获取学生信息，并返回学生信息的字典的列表
#         ....
#     2. 
#     def output_student(L):
#         # 以表格形式再打印学生信息
#         ...
#   验证测试：
#   　L = input_studnet()
#     output_student(L)
#     print("再添加几个学生信息")
#     L += input_student()
#     print("添加学生后的学生信息如下:")
#     output_student(L)

d8 = {}

def input_student(**kwargs):
	d8.update(kwargs)

def output_student():
	l8 = d8.keys()
	for x in l8:
		print(x,end="\t")
		for y in d8[x]:
			print(y,end="\t")
		else:
			print("\n")


# 输入学生的信息
input_student(jiangyu=['01',22,'男'],mly=['02',22,'女'],zhsan=['03',18,'男'],lisi=['04',18,'女'])
output_student()

	












