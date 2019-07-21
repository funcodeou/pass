x=0

while True:
	password = input('請輸入使用者密碼 :')
	x = x + 1
	if password == 'a123456':
		print('登入成功')
		break
	elif x == 1:
		print('密碼錯誤！還有2次機會')
	elif x == 2:
		print('密碼錯誤！還有1次機會')
	elif x == 3:
		print('密碼錯誤！你沒有機會了')
		break


