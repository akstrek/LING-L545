import sys, re

acrnym = ['etc.', 'e.g.', 'i.e.', 'D.']


text_line = sys.stdin.readline()

counter = 1


while text_line:
	text_line = text_line.strip()
	if text_line == '':	
		text_line = sys.stdin.readline()
		continue
    print('# sent_id =', counter)
	print('# text =',text_line)
	text_line = text_line.replace('(','( ')
    text_line = text_line.replace('[', '[ ')
	
    text_line = re.sub(r',([^0-9])',r', \g<1>', text_line)
	text_line = re.sub(r'([\[\]()"?:!;*])', r' \g<1>', text_line)
	text_line = re.sub(r'([^0-9]),', r' \g<1> ,', text_line)
	
	text_line = re.sub(r'  +', ' ', text_line)
	counter = counter + 1
	counter = 1


	for tokenized in text_line.split(' '):
		if tokenized == '':
			continue
		if tokenized not in acrnym and tokenized [-1] == '.':
			series = (counter, tokenized [0:-1],'_','_','_','_','_','_','_','_')
			print('%d' %series)
			counter = counter + 1
			series = (counter, tokenized[-1],'_','_','_','_','_','_','_','_')
			print('%d' %series)	
		else:
			series = (counter, tokenized,'_','_','_','_','_','_','_','_')
			print('%d' %series)
		counter = counter + 1
	

	text_line = sys.stdin.readline() 
	print()