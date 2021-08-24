import os

def find_substring(text, query, start=0):
	position = 0
	for x in range(start,len(text)):
		if text[x] == query[0]:
			if text[x:x + len(query)] == query and position == 0:
				position = x + 1
	return position - 1

print("Function URLs :")
with open('url.txt', 'r') as fp:
    line = fp.readline()
    cnt = 1
    while line:
       print(line.strip())
       print("https://www.wolframalpha.com/input/?i=reals+roots+of+"+line.strip()[find_substring(line.strip(), "input=")+6:len(line.strip())])
       line = fp.readline()
       cnt += 1
print()
if os.path.isfile('roots.txt'):
        roots = []
        print("Roots :")
        with open('roots.txt', 'r') as fp:
            line = fp.readline()
            cnt = 1
            while line:
                roots.append(line.strip())
                line = fp.readline()
                cnt += 1
        print(roots)
        print()
print("----------------------------------")
print()
print("Functions java code :")
with open('functions.txt', 'r') as fp:
    line = fp.readline()
    cnt = 1
    while line:
       print(line.strip())
       line = fp.readline()
       cnt += 1
print()
print("Sections java code :")
print()
with open('sections.txt', 'r') as fp:
    line = fp.readline()
    cnt = 1
    while line:
       print(line.strip())
       line = fp.readline()
       cnt += 1
print()
print("Values java code :")
print()
with open('values.txt', 'r') as fp:
    line = fp.readline()
    cnt = 1
    while line:
       print(line.strip())
       line = fp.readline()
       cnt += 1
print()
print("Rescaling java code :")
print()
with open('rescaling.txt', 'r') as fp:
    line = fp.readline()
    cnt = 1
    while line:
       print(line.strip())
       line = fp.readline()
       cnt += 1
