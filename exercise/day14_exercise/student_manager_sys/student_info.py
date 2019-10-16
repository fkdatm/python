# 该模块用于操作学生的信息

# 字典用于保存所有学生的信息
d_studentinfo = {}

# 此函数用于添加学生
def add_student():
	student_num = input("请输入学生学号：")
	student_name = input("请输入学生的姓名：")
	student_age = int(input("请输入学生的年龄："))
	student_sex = input("请输入学生的性别：")
	student_score = int(input("请输入学生的分数："))
	l_studentinfo = [student_name,student_age,student_sex,student_score]
	d_studentinfo[student_num] = l_studentinfo
	print("\n已成功添加学生信息！")
	


# 此函数用于查询学生信息
def select_student():
	print("请选择：")
	option = input("1:查看某个学生信息		2:查看所有学生信息\n")
	if option == "1":
		student_num = input("请输入学生的学号：")
		l_stunums = d_studentinfo.keys()
		if student_num in l_stunums:
			print(student_num,end="  ")
			for stuinfo in d_studentinfo[student_num]:
				print(stuinfo,end="  ")
			else:
				print("\n\n")
	elif option == "2":
		for student_num in d_studentinfo.keys():
			print(student_num,end="  ")
			for stuinfo in d_studentinfo[student_num]:
				print(stuinfo,end="  ")
			else:
				print("\n")
	else:
		print("输入无效！")



# 此函数用于修改学生信息
def update_student():
	stunum = input("请输入学生学号：")
	l_stunums = d_studentinfo.keys()
	if stunum in l_stunums:
		
		l_stuinfo = d_studentinfo[stunum]
		
		print('''
		1.修改学生成绩
		
		2.修改学生姓名
		
		3.修改学生年龄
		
		''')
		
		option = int(input("请选择需要进行的操作："))
		
		if option == 1:
			stu_score = float(input("请输入分数："))
			l_stuinfo[3] = stu_score
			d_studentinfo[stunum] = l_stuinfo
			print("\n已更新成功！")
		elif option == 2:
			stu_name = input("请输入姓名：")
			l_stuinfo[0] = stu_name
			d_studentinfo[stunum] = l_stuinfo
			print("已更新成功！")
		elif option == 3:
			stu_age = int(input("请输入年龄："))
			l_stuinfo[1] = stu_age
			d_studentinfo[stunum] = l_stuinfo
			print("\n已经更新成功！")
		else:
			print("\n输入不合法！！")
	else:
		print("\n没有该学生的信息！")
	
	


# 此函数用于删除学生的信息
def delete_stu():
	stunum = input("请输入学生学号：")
	l_stunums = d_studentinfo.keys()
	if stunum in l_stunums:
		d_studentinfo.pop(stunum)
		print("\n删除成功！")
	else:
		print("\n没有该学生的信息！")
		
		
	
	
	
	
	
	
	
	
	
	
	
	
	
	