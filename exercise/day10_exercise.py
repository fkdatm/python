print("-------------------------------------------第一题-------------------------------------\n")
# 1.写一个计算器解释执行器:
#   已知有如下函数:
#     def myadd(x, y):  # 计算两个数相加
#         return x + y
#     def mymul(x, y):  # 计算两个数相乘
#         return x * y
# 
#     def get_op(s): # s 代表操作字符串:'加','乘'
#         此处自己实现

def myadd(x,y):
	return x+y

def myminus(x,y):
	return x-y

def mymul(x,y):
	return x*y
	
def mydivide(x,y):
	return y/x

def get_op(s):
	
	l1 = s.split(" ")
	
	s1_a = int(l1[0])
	s1_opera = l1[1]
	s1_b = int(l1[2])

	if s1_opera == "加":
		print("结果是：",myadd(s1_a,s1_b))
	elif s1_opera == "减":
		print("结果是：",myminus(s1_a,s1_b))
	elif s1_opera == "乘":
		print("结果是：",mymul(s1_a,s1_b))
	elif s1_opera == "除":
		print("结果是：",mydivide(s1_a,s1_b))
	else:
		print("对不起，您输入的不合法！")
		

s1 = input("请输入需要进行的运算(加、减、乘、除)(如 10 加 20, 10 除 20)：\n")

get_op(s1)



print("\n\n-------------------------------------------第二题-------------------------------------\n")
# 2.写一个lambda表达式，判断这个数的2次方+1是否能被5整除,如果能整除返回True, 否则返回False
# 
# fx = lambda n: ....
# print(fx(3)) # True
# print(fx(4)) # False

f2 = lambda n: True if (n**2+1) % 5 == 0 else False

print(f2(3))	# True
print(f2(4))	# False



print("\n\n-------------------------------------------第三题-------------------------------------\n")
# 3. 写一个lambda表达式，求两个变量的最大值:
#    def mymax(x, y):
#        ....
#    # 或用lambda
#    mymax = lambda ....
#    print(mymax(100, 200))  # 200

lamd3 = lambda x,y : x if x > y else y

s3_1 = int(input("请输入第一个数："))
s3_2 = int(input("请输入第二个数："))

print("最大值为：",lamd3(s3_1,s3_2))



print("\n\n-------------------------------------------第四题-------------------------------------\n")
# 4. 写一个函数mysum(n),要求给出一个数n,求 
#    1 + 2 +3 + 4 + ..... + n 的和
#   如:
#     print(mysum(100))  # 5050
#     print(mysum(10))  # 55

def mycount(n):
	count = 0
	for x in range(1,n+1):
		count += x
	
	return count

s4 = int(input("请输入一个整数："))

print("结果是：",mycount(s4))



print("\n\n-------------------------------------------第五题-------------------------------------\n")
# 5. 写一个函数myfac(n)来计算n!(n的阶乘)
#   n! = 1*2*3*4*....*n
#   如:
#     print(myfac(5))  # 120
#     print(myfac(4))  # 24

def myfac(n):
	result = 1
	for x in range(1,n+1):
		result *= x
	
	return result

s5 = int(input("请输入一个整数："))
print("该数的阶乘是：",myfac(s5))



print("\n\n-------------------------------------------第六题-------------------------------------\n")
# 6. 写一个函数，求
#     1 + 2**2 + 3**3 + ... + n**n的和
#     (n给个小点的数)

def myfun6(n):
	count = 0
	for x in range(1,n+1):
		count += (x*x)
	
	return count
	
s6 = int(input("请输入一个整数："))
print("结果是：",myfun6(s6))



print("\n\n-------------------------------------------第七题-------------------------------------\n")
# 7. 修改之前的学生信息管理程序，实现添加菜单和选择菜单操作功能:
#    菜单:
#      +-----------------------------+
#      |  1) 添加学生信息              |
#      |  2) 查看所有学生信息          |
#      |  3) 修改学生的成绩            |
#      |  4) 删除学生信息              |
#      |  q) 退出                     |
#      +-----------------------------+
#    请选择: 1
#      请输入姓名:....
#    请选择: 3
#      请输入修改学生的姓名: ....
#   (要求每个功能都对应一个函数)
d7_student = {}


		


def add_student():
	s7_name = input("请输入学生姓名：")
	s7_num = input("请输入学生的学号：")
	s7_age = int(input("请输入学生的年龄："))
	s7_score = int(input("请输入学生的分数："))
	s7_sex = input("请输入学生的性别(男/女)：")		
	l7_stuinfo = []
	l7_stuinfo.append(s7_name)
	l7_stuinfo.append(s7_age)
	l7_stuinfo.append(s7_score)
	l7_stuinfo.append(s7_sex)
	d7_student[s7_num] = l7_stuinfo
		

def select_student():
	while True:
		s7_option = int(input("查看所有学生请输入：1   查询单个学生信息请输入：2\n"))
		l7_stunums = d7_student.keys()
		if s7_option == 1:
			for num in l7_stunums:
				print(num,end=" ")
				l7_stuinfos = d7_student[num]
				for l7_stuinfo in  l7_stuinfos:
					print(l7_stuinfo,end=" ")
				
				print("\n\n")
			return
		elif s7_option == 2:
			s7_stunum = input("请输入学生学号：\n")
			if s7_stunum in l7_stunums:
				print(s7_stunum,end=" ")
				l7_stuinfos = d7_student[s7_stunum]
				for l7_stuinfo in  l7_stuinfos:
					print(l7_stuinfo,end=" ")
				
				print("\n\n")
			else:
				print("没有该学生的信息！")
			
			return
		else:
			s7_input = int(input("输入不合法！ 重新输入请输入：1  ，退出请输入：2\n"))
			if s7_input == 1:
				continue
			elif s7_input == 2:
				return
			else:
				print("输入错误，即将退出！")
				return
				
def update_score():
	l7_stunums = d7_student.keys()
	s7_stunum = input("请输入学生的学号：")
	if s7_stunum in l7_stunums:
		l7_stuinfo = d7_student[s7_stunum]
		s7_stuscore = int(input("请输入新的分数："))
		l7_stuinfo[2] = s7_stuscore
		d7_student[s7_stunum] = l7_stuinfo
		print("已经更新完毕！！")
	else:
		print("没有该学生的信息")


def remove_stu():
	l7_stunums = d7_student.keys()
	l7_stunum = input("请输入要移除的学生学号：")
	if l7_stunum in l7_stunums:
		d7_student.pop(l7_stunum)
		print("删除完毕！！")
	else:
		print("没有该学生过的信息，不用删除。")
		
def menu():
	while True:
		print('''
		\n
		1) 添加学生信息
		2) 查看学生信息
		3) 修改学生的成绩
		4) 删除学生信息
		q) 退出
		\n
		''')
		
		s7_option = input("请选择需要进行的操作：")
		if s7_option == "1":
			add_student()
		elif s7_option == "2":
			select_student()
		elif s7_option == "3":
			update_score()
		elif s7_option == "4":
			remove_stu()
		elif s7_option == "q":
			break
		else:
			print("请输入菜单中的选项！！！\n\n")


menu()

