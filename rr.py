import random
r = random.randint (1, 100)
while True:
	x = input ('請輸入數字： ')
	if int(x) == r:
		print ('答對了！')
		break
	elif int(x) > r:
		print ('比答案大! 答案是', r)
	elif int(x) < r:
		print ('比答案小')