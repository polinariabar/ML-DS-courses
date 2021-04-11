def read_csv(name):
	with open(name, 'r') as fp:
		data = fp.read()
	print(data)
	return data

def replace_commas(data):
	word	= ""
	newData = ""

	for line in data.splitlines():
		print(line)
		quote = False
		for symb in line:
			if symb == '\"':
				if quote == False:
					quote = True
				else:
					quote = False
			if (symb == ',' and quote == False):
				newData += word + '\t'
				word = ""
			else:
				word += symb
		newData += 'aaaaa' + '\n'
	print(newData)

data = read_csv('d01_ds.csv')
replace_commas(data)




