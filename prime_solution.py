def prime_num(a):
	#a=int(raw_input('enter a: '))
	n = int(2)
	if a == 0 or a==1:
		return false
	elif a<2:
		return false
	elif n==2:
		while n<a:
			if a % n == 0:
				return false	
				break
				n= n+1
			else:
				return true






