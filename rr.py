import random
start = input ('請輸入開始範圍： ')
end  = input ('請輸入結束範圍： ')
start = int (start)
end  = int (end)
r = random.randint (start, end)
while True:
	x = input ('請輸入數字： ')
	if int(x) == r:
		print ('答對了！')
		break
	elif int(x) > r:
		print ('比答案大! 答案是', r)
	elif int(x) < r:
		print ('比答案小')