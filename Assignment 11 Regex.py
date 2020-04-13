import re
fh=open(r'C:\Users\Jake Wojcik\Documents\Py4e\regex_sum_373415.txt')
sum=0

for line in fh:
	num= re.findall('[0-9]+',line)
	for number in num:
		sum= sum+ int(number)
print(sum)