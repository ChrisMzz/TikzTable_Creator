import webbrowser

#IMPORTANT -- If this isn't Chrome's directory, or you don't have Chrome, edit the directory below to that of the browser you use and adapt the names accordingly.
webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))


#We need to first define functions to convert from decimal to binary and back. We will try to keep everything in string format.
def bin_to_dec(x):
	increment = 1
	decimal_number = 0
	for space in range(0,len(x)):
		decimal_number += increment * int(x[len(x) - space - 1])
		increment = increment * 2
	return decimal_number

def dec_to_bin(n):
	#This next line is necessary because we need to first convert the string into a number to analyze its structure.
	n = int(n)
	inc = 1
	bin_temp = ""
	while inc <= n:
		inc = inc*2
	while inc > 1:
		inc = inc/2
		if n // inc == 1:
			bin_temp += "1"
			n -= inc
		else:
			bin_temp += "0"
	return bin_temp

def dec_to_bin_8(n):
	bin_temp = ""
	n = str(dec_to_bin(n))
	length = 8 - len(n)
	for x in range(length):
		bin_temp += "0"
	bin_temp += n
	return bin_temp

#print(dec_to_bin_8(bin_to_dec("1011")))
#print(bin_to_dec(dec_to_bin("11")))

Base64_index_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
ASCII = {" ":"32", "!":"33", '"':"34", "#":"35", "$":"36", "%":"37", "&":"38", "'":"39", "(":"40", ")":"41", "*":"42",  "+":"43", ",":"44", "-":"45", ".":"46", "/":"47", "0":"48", "1":"49", "2":"50", "3":"51", "4":"52", "5":"53", "6":"54", "7":"55", "8":"56", "9":"57", ":":"58", ";":"59", "<":"60", "=":"61", ">":"62", "?":"63", "@":"64", "A":"65", "B":"66", "C":"67", "D":"68", "E":"69", "F":"70", "G":"71", "H":"72", "I":"73", "J":"74", "K":"75", "L":"76", "M":"77", "N":"78", "O":"79", "P":"80", "Q":"81", "R":"82", "S":"83", "T":"84", "U":"85", "V":"86", "W":"87", "X":"88", "Y":"89", "Z":"90", "[":"91", "\\":"92", "]":"93", "^":"94", "_":"95", "`":"96", "a":"97", "b":"98", "c":"99", "d":"100", "e":"101", "f":"102", "g":"103", "h":"104", "i":"105", "j":"106", "k":"107", "l":"108", "m":"109", "n":"110", "o":"111", "p":"112", "q":"113", "r":"114", "s":"115", "t":"116", "u":"117", "v":"118", "w":"119", "x":"120", "y":"121", "z":"122", "{":"123", "|":"124", "}":"125", "~":"126"}
index_table = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


def URL_encrypt(text):
    coded = "real+roots+of+"
    for i in range(0, len(text)):
        coded += "%" + dec_to_anything(int(ASCII[text[i:i+1]]), 16)
    return coded

def b64_encrypt(text):
	special_car = len(text) % 3
	coded = ""
	for i in range(0, len(text) // 3):
		temp_bin = dec_to_bin_8(ASCII[text[i*3]]) + dec_to_bin_8(ASCII[text[i*3 + 1]]) + dec_to_bin_8(ASCII[text[i*3 + 2]])
		coded = coded + Base64_index_table[int(bin_to_dec(temp_bin[0:6]))] + Base64_index_table[int(bin_to_dec(temp_bin[6:12]))] + Base64_index_table[int(bin_to_dec(temp_bin[12:18]))] + Base64_index_table[int(bin_to_dec(temp_bin[18:24]))]
	if special_car == 1:
		special_coded = dec_to_bin_8(ASCII[text[len(text) - 1]])
		while len(special_coded) != 24:
			special_coded += "0"
		coded = coded + Base64_index_table[int(bin_to_dec(special_coded[0:6]))] + Base64_index_table[int(bin_to_dec(special_coded[6:12]))] + "=" + "="
		return coded
	elif special_car == 2:
		special_coded = dec_to_bin_8(ASCII[text[len(text) - 2]]) + dec_to_bin_8(ASCII[text[len(text) - 1]])
		while len(special_coded) != 24:
			special_coded += "0"
		coded = coded + Base64_index_table[int(bin_to_dec(special_coded[0:6]))] + Base64_index_table[int(bin_to_dec(special_coded[6:12]))] + Base64_index_table[int(bin_to_dec(special_coded[12:18]))] + "="
		return coded
	else:
		return coded



def dec_to_anything(n, m, anyn=""):
	n = int(n)
	if n // m > m-1:
		anyn = dec_to_anything(n//m, m, anyn)
	else:
		anyn += index_table[n//m]
	anyn += index_table[n%m]
	return anyn

with open('rawfunctions.txt', 'r') as fp:
	line = fp.readline()
	cnt = 1
	while line:
		webbrowser.get('chrome').open(f"https://www.wolframalpha.com/input/?i=reals+roots+of+{URL_encrypt(line.strip())}")
		print(f"http://api.wolframalpha.com/v2/query?appid=X7YYYW-EXUUG37A4K&input={URL_encrypt(line.strip())}")
		line = fp.readline()
		cnt += 1
