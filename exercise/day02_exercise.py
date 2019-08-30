# 第二天的练习题

# 1. 北京出租车计费
#   收费标准:
#     3公里以内收费13元
#     超过3公里后基本单价为 2.3元/公里
#     空驶费: 超过15公里后，每公里加收基本单价的50%作为返程的空驶费(3.45元/公里)
#   要求：
#     输入公里数，打印出费用的金额(以元为单位进行四舍五入)
print("==========================Day02练习题第一题=============================")

km = int(input("请输入公里数：")) or -1
if km<=0:
	print("您输入的公里数不和法")
elif km<3:
	println("您的本次行程计费为",13,sep='：')
elif km<15:
	print("您的本次行程计费为",(13+(km-3)*2.3),sep='：')
else:
	print("您的本次行程计费为",(13+(15-3)*2.3+(km-15)*(2.3*1.5)),sep=':')
	
# 2. 输一个学生的三科成绩：
#    1. 打印出最高分是多少分
#    2. 打印出最低分是多少分
#    3. 打印出平均分是多少分
print("==========================Day02练习题第二题=============================")
chineseScore=int((input("请输入语文成绩:") or 0))
mathScore=int((input("请输入数学成绩:") or 0))
englishScore=int((input("请输入英语成绩:") or 0))
top_score = None
low_score = None
avg_score = (chineseScore+mathScore+englishScore)/3
# print("您的最高分是",(englishScore if englishScore >= (chineseScore if chineseScore >= mathScore else mathScore) else (chineseScore if chineseScore >= mathScore else mathScore)),sep=':')

if chineseScore>mathScore and chineseScore>englishScore:
	top_score = chineseScore
	low_score = mathScore if englishScore>mathScore else englishScore
elif mathScore>chineseScore and mathScore>englishScore:
	top_score = mathScore
	low_score = chineseScore if englishScore>chineseScore else englishScore
else:
	top_score = englishScore
	low_score = chineseScore if mathScore>chineseScore else mathScore

# print("您的最高分是",(englishScore if englishScore >= (chineseScore if chineseScore >= mathScore else mathScore) else (chineseScore if chineseScore >= mathScore else mathScore)),sep=':')
print("您的最高分是",top_score,sep=':')
print("您的最低分是",low_score,sep=':')
print("您的平均分是",avg_score,sep=':')


print("==========================Day02练习题第三题=============================")
# 3. 给出一个年份，判断是否为闰年并打印结果
#   闰年规则: 每四年一闰，每百年不闰，四百年又是一个闰年
#   例:
#     2016年 闰年 
#     2100年 不是闰年
#     2400年 是闰年

year = int(input("请输入年份"))
if year%4==0 and year%400!=0:
	print("您输入的年份是润年")
else:
	print("您输入的年份不是润年")

print("==========================Day02练习题第四题=============================")

# 4 BMI 指数(Body Mass Index) 以称身体质量指数
#   BMI值计算公式: 
#        BMI = 体重(公斤)/ 身高(米)的平方
#   例如:
#      一个69公斤的人，身高是 173公分
#      BMI = 69 / 1.73 ** 2 = 23.05
#   标准表:
#      BMI < 18.5        体重过轻
#      18.5 <= BMI <= 24 正常范围
#      BMI > 24          体重过重（超标)
#   输入身高和体重，打印BMI值，并打印体重状况
height = int(input("请输入身高:"))
weight = int(input("请输入体重(公斤):"))
bmi = weight / height ** 2
print("您的BMI值是",bmi,sep=':',end='	')
if bmi<18.5:
	print("您的体重有点过轻了呢！")
elif bmi<24:
	print("您的体重很正常呢！")
else:
	print("您的体重有点偏重了呢！")
