import urllib.request

def find_substring(text, query, start=0):
	position = 0
	for x in range(start,len(text)):
		if text[x] == query[0]:
			if text[x:x + len(query)] == query and position == 0:
				position = x + 1
	return position - 1

def newify(text, query, replace=""):
    start = 0
    newtext = ""
    while find_substring(text + query, query, start) != -1:
        if (start == 0):
            newtext = newtext + text[start:find_substring(text + query, query, start)]
        else:
            newtext = newtext + replace + text[start:find_substring(text + query, query, start)]
        start = find_substring(text + query, query, start) + 1
    return newtext


def startswith(text, prefix):
	start = 1
	for p in range(0,len(prefix)):
		if text[p] != prefix[p]:
			start = 0
	if start == 1:
		return True
	else:
		return False

def URL_encrypt(text):
    coded = ""
    for i in range(0, len(text)):
        coded += "%" + dec_to_anything(int(ASCII[text[i:i+1]]), 16)
    return coded

def dec_to_anything(n, m, anyn=""):
	n = int(n)
	if n // m > m-1:
		anyn = dec_to_anything(n//m, m, anyn)
	else:
		anyn += index_table[n//m]
	anyn += index_table[n%m]
	return anyn

ASCII = {" ":"32", "!":"33", '"':"34", "#":"35", "$":"36", "%":"37", "&":"38", "'":"39", "(":"40", ")":"41", "*":"42",  "+":"43", ",":"44", "-":"45", ".":"46", "/":"47", "0":"48", "1":"49", "2":"50", "3":"51", "4":"52", "5":"53", "6":"54", "7":"55", "8":"56", "9":"57", ":":"58", ";":"59", "<":"60", "=":"61", ">":"62", "?":"63", "@":"64", "A":"65", "B":"66", "C":"67", "D":"68", "E":"69", "F":"70", "G":"71", "H":"72", "I":"73", "J":"74", "K":"75", "L":"76", "M":"77", "N":"78", "O":"79", "P":"80", "Q":"81", "R":"82", "S":"83", "T":"84", "U":"85", "V":"86", "W":"87", "X":"88", "Y":"89", "Z":"90", "[":"91", "\\":"92", "]":"93", "^":"94", "_":"95", "`":"96", "a":"97", "b":"98", "c":"99", "d":"100", "e":"101", "f":"102", "g":"103", "h":"104", "i":"105", "j":"106", "k":"107", "l":"108", "m":"109", "n":"110", "o":"111", "p":"112", "q":"113", "r":"114", "s":"115", "t":"116", "u":"117", "v":"118", "w":"119", "x":"120", "y":"121", "z":"122", "{":"123", "|":"124", "}":"125", "~":"126"}
index_table = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"



finalroots = []
root_dictionary = {}

with open('url.txt', 'r') as fp:
    line = fp.readline()
    cnt = 1
    while line:
        try:
            with urllib.request.urlopen(line.strip()) as f:
                roots = []
                url = f.read().decode('utf-8')
                url = url[find_substring(url, "Result"):find_substring(url, "Root plot")]
                while find_substring(url, "<plaintext>x = ") != -1:
                    roots.append(url[find_substring(url, "<plaintext>x = ")+15:find_substring(url, "</plaintext>", find_substring(url, "<plaintext>x = "))])
                    url = url[find_substring(url, "</plaintext>", find_substring(url, "<plaintext>x = ")):len(url)]
                
                for element in roots:
                    if startswith(element, "±"):
                        roots.append(element[1:len(element)])
                        ptent = "-("+element[1:len(element)]+")"
                        with urllib.request.urlopen(f"http://api.wolframalpha.com/v2/query?appid=X7YYYW-EXUUG37A4K&input={URL_encrypt(ptent)}") as g:
                            opposite = g.read().decode('utf-8')
                            roots.append(opposite[find_substring(opposite, 'alt=')+5:find_substring(opposite, 'title',find_substring(opposite, 'alt='))-9])
                        roots.remove(element)
                for element in roots:
                    newify(element, " ")
                    finalroots.append(float(newify(element, "^", "**")))
                    root_dictionary[float(newify(element, "^", "**"))] = element
                finalroots.sort()
        except urllib.error.URLError as e:
                print(e.reason)
        line = fp.readline()
        cnt+=1

for i in range(0, len(finalroots)):
    print(root_dictionary[finalroots[i]])
