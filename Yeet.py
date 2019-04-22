import sys
###---Open the file---###
if len(sys.argv) == 2:
	try:
		yeetFile = open(sys.argv[1], 'r')
	except:
		print('Error opening ' + sys.argv[1])
else:
	print('Usage: python3 ' + sys.argv[0] +  ' filename')

###---Setup the file---###
code = []
for word in yeetFile.read().split():
	code.append(word)
###---Loop Addresses---###
loop = {}
temp = code.copy()

for i in range(len(temp)-1, -1, -1):
	if temp[i] == 'Yeeeeet':
		for j in range(i, len(temp)):
			if temp[j] == 'yeeeeet':
				loop[i] = j
				temp[i] = 0 
				temp[j] = 0
				break

###---Begin executing---###
memory = [0]
ptr = 0
codePtr = 0


while codePtr < len(code):
	if code[codePtr] =='Yeet':
		ptr+=1
		if ptr == len(memory):
			memory.append(0)	#if only this worked in the real world
	elif code[codePtr] == 'yeet':
		if ptr > 0:
			ptr-=1
	
	elif code[codePtr] == 'Yeeet':
		memory[ptr] +=1 #should this be capped?
	elif code[codePtr] == 'yeeet':
		if memory[ptr] > 0:
			memory[ptr] -=1

	elif code[codePtr] == 'Yeeeet':
		sys.stdout.write(chr(memory[ptr]))
	elif code[codePtr] == 'yeeeet':
		memory[ptr] = sys.stdin.read(1)

	elif code[codePtr] == 'Yeeeeet':
		if memory[ptr] == 0:
			codePtr = loop.get(codePtr)
	elif code[codePtr] == 'yeeeeet':
			for i in loop:
				if loop[i] == codePtr:
					codePtr = i -1
					break
	else:
		print('Invalid syntax at ', codePtr)
	codePtr+= 1







