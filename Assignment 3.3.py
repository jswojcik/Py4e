try:
	sc = input("Enter your score between 0.0 and 1.0 ")
	score = float(sc)
	if score> 1.0:
		print('invalid')
	elif score >= 0.9:
		print('A')
	elif score >= 0.8:
		print('B')
	elif score >= 0.7:
		print('C')
	elif score < 0.6:
		print('F')
except:

		print('insert numeric')
