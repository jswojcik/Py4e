name = input("Enter file:")
if len(name) < 1: name = r"C:\Users\Jake Wojcik\Documents\Py4e\mbox-short.txt"
fh = open(name)
di = dict()


for line in fh:
	if not line.startswith('From '):continue
	wds=line.split()
	hour=wds[5].split(':')

	di[hour[0]]=di.get(hour[0],0)+1

#### count sorted by hour

lst=list()


for k,v in di.items():
	lst.append((k,v))
lst.sort()
for hour, count in lst:
	print(hour, count)


