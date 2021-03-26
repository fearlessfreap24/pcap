from os import strerror

f = input("Please type Prof Jekyll's file name: ")

students = {}
try:
    with open(f, 'r') as stream:
        line = stream.readline()
        while line:
            split_line = line.split()
            if f'{split_line[0]}_{split_line[1]}' in students:
                students[f'{split_line[0]}_{split_line[1]}']['points'] += float(split_line[2])
            else:
                students[f'{split_line[0]}_{split_line[1]}'] = {'first': split_line[0], 'last':split_line[1], 'points': float(split_line[2])}
            line = stream.readline()

except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
    exit(e.errno)

for student in sorted(students.keys()):
    print(students[student]['first'], students[student]['last'], students[student]['points'])