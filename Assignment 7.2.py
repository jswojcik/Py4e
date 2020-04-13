# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
tot = 0
for line in fh:
	if not line.startswith("X-DSPAM-Confidence:"): continue
	pos = line.find(' ')
	num = line[pos:]
	num = float(num)

	count = count + 1
	tot = num + tot
	print(tot)
	ans = tot / count

print("Average spam confidence:", ans)
