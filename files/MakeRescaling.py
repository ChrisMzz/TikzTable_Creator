import csv

x = 0
with open('rescaling_info.csv', 'r') as fp:
    reader = csv.reader(fp)
    for row in reader:
        if str(row[0]) == ".":
            y=""
            if x == 1:
                y=1
        else:
            y=str(row[0])
        if x == 0:
            print(f"TikzText image = new TikzText({y});")
        if x == 1:
            print(f"image.setCustomSpace({y});")
        if x == 2:
            print("Table table = new Table(functions, sections, values);")
        if x == 3:
            print(f"image.printTable(table, {y});")
        x+=1