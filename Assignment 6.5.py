text = "X-DSPAM-Confidence:    0.8475";
atpos= text.find('0')
float(atpos)
sppos=text.find('5')
float(sppos)
host=text[atpos : sppos+1]
print(host)
