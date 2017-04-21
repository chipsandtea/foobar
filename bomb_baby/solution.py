def generate():
	m = 1
	f = 1
	flag = True
	for i in range(10):
		if flag:
			m += f
			print(str(m) + " " + str(f))
			flag = False
		else:
			f += m
			print(str(f) + " " + str(m))
			flag = True

generate()