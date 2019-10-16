# 本模块主要是菜单选项

import student_info

def menu():
	while True:
		print('''
		
		1.增加学生信息
		
		2.查询学生信息
		
		3.修改学生信息
		
		4.删除学生信息
		
		q.退出


		''')
		
		option = input("请选择需要进行的操作：")
		
		if option == "1":
			student_info.add_student()
		elif option == "2":
			student_info.select_student()
		elif option == "3":
			student_info.update_student()
		elif option == "4":
			student_info.delete_stu()
		elif option == "q":
			return	
		else:
			print("输入无效，请按规定输入！！")
			

menu()