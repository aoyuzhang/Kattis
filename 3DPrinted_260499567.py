numberOfStatues=int(input());
nofDays=0;
numberOfPrinters=1;
while numberOfPrinters < numberOfStatues:
	numberOfPrinters=numberOfPrinters*2;
	nofDays=nofDays+1;
print (nofDays+1);