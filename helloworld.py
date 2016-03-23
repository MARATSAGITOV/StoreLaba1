print ("Добро пожаловать!\nВыберите пункт:\n1. Продажа товара\n2. Поставка товара \n3. Данные по продажам")
a = int(input())
if a == 1 :	
	book = open ('склад.txt','r+')
	st = book.readlines()
	print("Хотите заказать?Д/Н")
	answer = input()
	while answer == 'Д':
		for i in st:
			print(i)
		count = 0	
		print("Введите ID и количество единиц")
		N = input()
		Q = int(input())
		for i in st:
			i = i.split(',')
			if N == i[0] and Q <= int(i[3]):
				print('спасибо за заказ!')
				st[count] = st[count].split(',')
				i[3] = str(int(i[3]) - Q) + '\n'
				st[count] = i[0] + ',' + i[1] + ',' + i[2] + ',' + i[3]
				st += str(i[0]) + ',' + str(int(i[2])*int(i[3])) + 'руб' + '\n'
				with open('склад.txt', 'w') as book:
					for i in st:
						book.writelines(i) 
				with open('продажи.txt', 'w') as book:
					for j in st:
						book.writelines(j)
				answer = input('Желаете повторить ввод?\nД-да\nН-нет')
				break
			else:
				count += 1
		
		
elif a == 2 :
	book = open ('склад.txt','r+')
	st = book.readlines()
	for i in st:
		print(i)
	print("Введите ID ...")
	iden = input()
	count = 0
	flag = False	
	for i in st:
		i = i.split(',')
		if iden == i[0] :
			print(" количество товара")
			q = int(input())
			i[3] = str(int(i[3])+q)
			st[count] = i[0] + ',' + i[1] + ',' + i[2] + ',' + i[3] + '\n'
			flag = True
			with open('склад.txt', 'w') as book:
				for i in st:
					book.writelines(i)
		else:
			count += 1	
		if flag:
			break
		new = input('такого айди нет')
		st += iden + ',' + new + '\n'
		with open('склад.txt', 'w') as book:
			for i in st:
				book.writelines(i)
elif a == 3 :
	book = open ('продажи.txt','r')
	st = book.readlines()
	for i in st:
		print(i)

