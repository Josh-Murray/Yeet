import sys

###---Usage---###
#python3 Translator.py -y2b output
if len(sys.argv) == 4:
	try:
		data = open(sys.argv[2], 'r')
		out = open(sys.argv[3], 'w+')
	except:
		print('Error opening ' + sys.argv[1])
elif '-h' in sys.argv:
	print('Usage: python3 ' + sys.argv[0] +  ' -Pattern ' + 'Input ' + 'Output')
	print(' -y2b\t Converts Yeet to brainfuck')
	print(' -b2y\t Converts brainfuck to Yeet')
	
else:
	print('Usage: python3 ' + sys.argv[0] +  ' -Pattern ' + 'Input ' + 'Output')
	print('Use -h for list of -Patterns')

if sys.argv[1] =='-y2b':
	text = data.read()
	text = text.replace('Yeet ', '>')
	text = text.replace('yeet ', '<')
	text = text.replace('Yeeet ', '+')
	text = text.replace('yeeet ', '-')
	text = text.replace('Yeeeet ', '.')
	text = text.replace('yeeeet ', ',')
	text = text.replace('Yeeeeet ', '[')
	text = text.replace('yeeeeet ', ']')
	out.write(text)
elif sys.argv[1] == '-b2y':
	text = data.read()
	
	text = text.replace('>','Yeet ')
	text = text.replace('<','yeet ')
	text = text.replace('+','Yeeet ')
	text = text.replace('-','yeeet ')
	text = text.replace('.','Yeeeet ')
	text = text.replace(',','yeeeet ')
	text = text.replace('[','Yeeeeet ')
	text = text.replace(']','yeeeeet ')
	out.write(text)
	
	
