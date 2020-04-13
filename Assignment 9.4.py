name = input("Enter file:")
if len(name) < 1: name = r"C:\Users\Jake Wojcik\Documents\Py4e\mbox-short.txt"
fh = open(name)
di = dict()


for line in fh:
	if not line.startswith('From '):continue
	wds=line.split()
	wds=wds[1]


	#idiom: retireve/create/update counter
	di[wds]=di.get(wds,0)+1
		#print(w,'new',di[w])



#Find the most common word
largest =None
theword=None
for k,v in di.items():
	#print(k,v)
	if largest is None or v > largest:
		largest=v
		theword=k #capture/remember the word that was the largest
print(theword,largest)