import urllib.request, urllib.parse, urllib.error
fh=urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_42.html')

for line in fh:
	print(line.decode().strip())