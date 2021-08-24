import csv

def find_substring(text, query, start=0):
	position = 0
	for x in range(start,len(text)):
		if text[x] == query[0]:
			if text[x:x + len(query)] == query and position == 0:
				position = x + 1
	return position - 1

with open(f'sections.csv', 'r') as fp:
    reader = csv.reader(fp)
    section=""
    for row in reader:
        section+=row[0] + ", "
    section=section[0:len(section)-2]
    print(f'List<String> sections = List.of("{section}");')