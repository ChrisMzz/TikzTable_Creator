import csv

def find_substring(text, query, start=0):
	position = 0
	for x in range(start,len(text)):
		if text[x] == query[0]:
			if text[x:x + len(query)] == query and position == 0:
				position = x + 1
	return position - 1

def newify(text, query):
	start = 0
	newtext = ""
	while find_substring(text + query, query, start) != -1:
		newtext = newtext + text[start:find_substring(text + query, query, start)]
		start = find_substring(text + query, query, start) + 1
	return newtext

x=0


with open('values/length.txt', 'r') as fp:
    length_value = int(fp.read())

y=0
for x in range(1,length_value+1):
    value=""
    with open(f'values/values{x}.csv', 'r') as fp:
        reader = csv.reader(fp)
        for row in reader:
            value+=newify(newify(newify(str(row),"'"),"["),"]")+", "
        value=value[y:len(value)-2]
        y=len(value)+2
        print(f'values.add("{value}");')