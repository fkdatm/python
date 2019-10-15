print("-------------------------------------------第一题-------------------------------------\n")
# 1. 输入一个正方形的周长，输出正方形的面积
import math

def calculate_perimeter(n):
	side = n//4
	print("正方形的面积为：",math.pow(side,2))

s1 = int(input("请输入周长："))
calculate_perimeter(s1)


print("\n\n-------------------------------------------第二题-------------------------------------\n")
# 2. 输入一个圆的半径，打印出这个圆的面积

def calculate_area(n):
	print("圆的面积为：",math.pi*math.pow(n,2))
	
s2 = int(input("请输入圆的半径："))
calculate_area(s2)



print("\n\n-------------------------------------------第三题-------------------------------------\n")
# 3. 输入一个正方形的面积，打印这个正方型的周长
#    ( 要求: 用math模块内的函数和数据)

s3 = int(input("请输入正方形的面积："))
print("该正方形的周长为：",math.sqrt(s3)*4)


print("\n\n-------------------------------------------第四题-------------------------------------\n")
# 4. 写一个程序，输入你的出生日期
#   1) 算出你已经出生了多少天?
#   2) 算出你出生那天是星期几?
import time
s4 = input("请输入您的出生日期(示例:1997-6-7)：")
l4 = s4.split("-")
s4_year = int(l4[0])
s4_month = int(l4[1])
s4_day = int(l4[2])

# 得到当前的utc时间秒数
s4_nowtime_sec = time.time()

# 得到出生时的utc时间秒数
s4_birthday_sec = time.mktime((s4_year,s4_month,s4_day,0,0,0,0,0,0))

print("您已经出生了 %d 天！" % ((s4_nowtime_sec-s4_birthday_sec)/60/60//24) )

# 写一个字典存星期

d_week = {0:'星期一',
		  1:'星期二',
		  2:'星期三',
		  3:'星期四',
		  4:'星期五',
		  5:'星期六',
		  6:'星期天'
	}

s4_birthdaytup = time.localtime(s4_birthday_sec)

print("您出生的那天是：",d_week[s4_birthdaytup[6]])



print("\n\n-------------------------------------------第五题-------------------------------------\n")
# 5. 写一个程序，以电子时钟格式打印时间:
#     时间格式为:
#         HH:MM:SS
#     时间每隔一秒刷新一次

def clock(n):
	i = 0
	while i < n:
		# 获取当前时间
		s5_timetup = time.localtime()
		# 取出时，分，秒
		s5_hour = s5_timetup[3]
		s5_min = s5_timetup[4]
		s5_sec = s5_timetup[5]
		# 打印时间
		print("%2d:%2d:%2d" % (s5_hour,s5_min,s5_sec))
		# 程序睡眠一秒钟
		time.sleep(1)
		i += 1

s5_input = int(input("请输入打印时间次数："))
clock(s5_input)



print("\n\n-------------------------------------------第六题-------------------------------------\n")
# 6. 编写一个闹钟程序，启动时设置定时时间，到时候后打印出一句语，然后程序退出

# 函数输入参数是一个时间元组
def clock2(str_timetup):
	# 当前时间的 秒数
	s6_nowtime = time.mktime(time.localtime())
	
	# 设定时间的秒数
	s6_settime = time.mktime(str_timetup)
	
	# 计算时间差
	s6_time_delay = s6_settime - s6_nowtime
	
	# 程序休眠
	time.sleep(s6_time_delay)
	
	# 打印：
	print("闹钟响了！！！！")


s6_input = input("请设置闹钟时间(示例：hh:mm:ss)：")
l6_time = s6_input.split(":")
s6_hour = int(l6_time[0])
s6_min = int(l6_time[1])
s6_sec = int(l6_time[2])

s6_timetup = (2019,10,15,s6_hour,s6_min,s6_sec,0,0,0)

clock2(s6_timetup)



print("\n\n-------------------------------------------第七题-------------------------------------\n")
# 7. 请编写函数fun,其功能是计算下列多项式的和
#    sn = 1 + 1/1! + 2/2! + 3/3! + ... n/n!
#    计算n为100时的值
#   看一下求出来的和是什么?
#   (建议用math.factorial)

def fun(n):
	sn = 1
	for i in range(1,n+1):
		sn += i/(math.factorial(i))
	
	return sn
	
s7_input = int(input("请输入n的值："))
print("结果为：",fun(s7_input))

















