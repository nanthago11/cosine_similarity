import math 
import os
import collections 
import sys 
import re 


 
iFileNm=sys.argv[1]
DN1=sys.argv[2]
DN2=sys.argv[3]
iFile = open( os.path.join(os.getcwd() ,iFileNm ), "r") 
iFileFirstLine=iFile.readline()
iFileFirstLine=iFileFirstLine.replace('\n', '')
HeaderValues = list(iFileFirstLine.split("\t")) 
HeaderValues=[x.upper() for x in HeaderValues]
HeaderListValues=[]
for i in HeaderValues:
	if i != '':
		HeaderListValues.append(i)
xIndexlist=HeaderListValues.index(DN1)
xValueArray=[]
yIndexlist=HeaderListValues.index(DN2)
yValueArray=[]

iFile = open( os.path.join(os.getcwd() ,iFileNm ), "r") 
for xline in iFile:
	xline=xline.replace('\n', '')
	HeaderValues = list(xline.split("\t")) 
	#print (HeaderValues)
	remListFile = []
	for i in HeaderValues:
		if i != '':
			remListFile.append(i)
	xValueArray.append(remListFile[xIndexlist+1])
	yValueArray.append(remListFile[yIndexlist+1])

	
xValueArray.pop(0)
yValueArray.pop(0)

xArrFloats=[]
yArrFloats=[]
xArrFloats=[float(i) for i in xValueArray]
yArrFloats=[float(i) for i in yValueArray]


dotPrd =sum([x*y for x,y in zip(xArrFloats,yArrFloats)])
Xsq=0.0
for x in xArrFloats:
	Xsq=Xsq+x*x

ySq=0.0
for y in yArrFloats:
	ySq=ySq+y*y
SqDOne=math.sqrt(Xsq)
SqDTwo=math.sqrt(ySq)
CosValue=dotPrd/(SqDOne*SqDTwo)
print('Cosine Similarity from input is : ',CosValue)

iFile.close()

