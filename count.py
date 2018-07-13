import sys, os

os.system('./count.sh> output.txt')

wcfile = open("output.txt","r")
wcfile = wcfile.readlines()

lasttimefile = open("lasttime.txt","r")
lasttime = lasttimefile.readline()
lasttime = lasttime.split("\\n', '")

#This line sucks because I index the last item in the array to make it int-convertible.
#Would work better with regex or something else smarter, i don't fuckin know
lasttime[len(lasttime) - 1] = lasttime[len(lasttime) - 1][0:8]

count = 0

def percentChange(x1,x2):
	change = (x2 - x1) / x1 * 100
	if(change < 0):
		return str(change)
	else:
		return "+" + str(change)
	

for x in wcfile:
	x = x.replace("\n","")
	if(count % 3 == 0):
		print(x)
	else:
		if(count % 3 == 1):
			print(x + " lines")
		elif(count % 3 == 2):
			print(x + " char")
		x = int(x)
		ox = int(lasttime[count])
		print("\t(" + percentChange(x,ox) + "%)")
	count += 1

lasttimefile = open("lasttime.txt","w+")
lasttimefile.write(str(wcfile))
os.remove("output.txt")