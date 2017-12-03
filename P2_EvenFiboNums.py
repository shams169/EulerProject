def fibo_list(n):
	a, b = 0, 1
	result=[]
	if n==0:
		return None
	elif n==1:
		return 1
	else:
		result.append(a)
		result.append(b)
		for i in range(n):
			a, b = b, a+b
			result.append(a+b)
	return result

def fibo_sum_even(n):
	a, b = 0,1
	sum = 0
	if n==0:
		return None
	elif n==1:
		return 1
	else:
		# for i in range(n):
		# 	a, b = b, a+b
		# 	print("B: "+str(b))
		# 	if (a+b)%2 == 0:
		# 		sum +=b

		while(b < 4000000):
			a, b = b, a+b
			if(b%2) == 0:
				sum +=b
	return sum



def main():
	#print(fibo_list(10))
	print(fibo_sum_even(10))

if __name__ == '__main__':
	main()




