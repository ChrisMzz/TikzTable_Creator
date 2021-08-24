print("import java.util.ArrayList;\nimport java.util.HashMap;\nimport java.util.List;\n")
print()
print()
print()
print("public class Main {")
print("\tpublic static void main(String[] args) {")
print()	
print()
print("\t\t//Creates a HashMap of each target function, along with spacing adjustments for esthetic purposes.")
print("\t\tHashMap<String, String> functions = new HashMap<String, String>();")
print()
with open('functions.txt', 'r') as fp:
    line = fp.readline()
    cnt = 1
    while line:
       print(f"\t\t{line.strip()}")
       line = fp.readline()
       cnt += 1
print()
print()
print("\t\t//... There should be one more function above as there are lines of values below.")
print()
print("\t\t//Creates a List of values each function will take for each section. Values will be different for tables of signs (LIN) and tables of variation (VAR).")
print("\t\t\t// For LIN : a space means there will be nothing (between or on), - is a minus (between), + is a plus (between), z is a zero (on), h is a barred zone, d is a double-line (on).")
print("\t\t\t// For VAR : a space")
print("\t\tList<String> values = new ArrayList<String>();")
with open('values.txt', 'r') as fp:
    line = fp.readline()
    cnt = 1
    while line:
       print(f"\t\t{line.strip()}")
       line = fp.readline()
       cnt += 1
print("\t\t//Creates horizontal sections for default target values.")
with open('sections.txt', 'r') as fp:
    line = fp.readline()
    cnt = 1
    while line:
       print(f"\t\t{line.strip()}")
       line = fp.readline()
       cnt += 1
print()
print()
print("\t\t//Creates a TikzPicture image with global rescaling and custom spacing inside the table.")
with open('rescaling.txt', 'r') as fp:
    line = fp.readline()
    cnt = 1
    while line:
       print(f"\t\t{line.strip()}")
       line = fp.readline()
       cnt += 1
print()
print("\t}")
print("}")