


def computepay(h, r):



	if h > 40:

		return (40 * r + (h - 40) * 1.5 * r)

	else:

		return (h * r)

try:

	hrs = input("Enter Hours:")

	hour = float(hrs)
	r = input("please input your rate:")

	rate = float(r)
	p = computepay(hour, rate)
	print(p)
except:

	print("Please,input your numberic")