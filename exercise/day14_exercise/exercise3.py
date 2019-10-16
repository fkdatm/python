# 模拟斗地主发牌,牌共54张
#  黑桃('\u2660'), 梅花('\u2663'),方块('\u2665'),红桃('\u2666')
#  大小王
#  A2-10JQK
#  三个人玩，每个人发17张牌，底牌留三张
#  操作:
#    输入回车: 打印第一个人的17张牌
#    输入回车: .....二...........
#    输入回车: .....三...........
#    输入回车: 打印三张底牌

import random as R
import time
# 创造扑克牌

def poke_games1():
	l_poker = []
	l_type = ['\u2660','\u2663','\u2665','\u2666']
	
	for type in l_type:
		for num in range(1,14):
			if num == 1:
				l_poker.append((type+'A'))
			elif num == 11:
				l_poker.append((type+'J'))
			elif num == 12:
				l_poker.append((type+'Q'))
			elif num == 13:
				l_poker.append((type+'K'))
			else:
				l_poker.append((type+str(num)))
	
	l_poker.append("Jocker")	# 大王
	l_poker.append("jocker")	# 小王
	
	
	print("正在洗牌...")
	R.shuffle(l_poker)
	time.sleep(5)
	
	print("开始发牌...")
	
	time.sleep(2)
	
	print("第一个人的牌：",end=" ")
	for x in range(0,17):
		print(l_poker[x],end=",")
	else:
		print("\n")
		
	print("第二个人的牌：",end=" ")
	for x in range(17,34):
		print(l_poker[x],end=",")
	else:
		print("\n")
		
	print("第三个人的牌：",end=" ")
	for x in range(34,51):
		print(l_poker[x],end=",")
	else:
		print("\n")
		
	print("底牌是：",end=" ")
	print(l_poker[51],l_poker[52],l_poker[53],sep=",")



#  改版之后：
print("第二版")
def get_poke():
    '''生成一副扑克'''
    kinds = ['\u2660', '\u2663', '\u2665', '\u2666']
    number = ['A'] + list(
        map(str, range(2, 11))) + list('JQK')
    # print(number)
    L = ['大王', '小王'] + [x + y for x in kinds
             for y in number]
    return L




def poke_games():
    pk = get_poke()
    R.shuffle(pk)
    input("输入回车继续")
    print("第一个人的17张牌是:", pk[:17])
    input("输入回车继续")
    print("第二个人的17张牌是:", pk[17:34])
    input("输入回车继续")
    print("第三个人的17张牌是:", pk[34:51])
    input("输入回车继续")
    print("底牌是:", pk[51:])



poke_games()

