__author__ = 'soroush'

fo = open('raw_data.data')
fo2 = open('data.txt', 'w')
lines = 0
for line in fo:
    if 'L' in line:
        new_line = line.replace('L', '1')
    elif 'B' in line:
        new_line = line.replace('B', '2')
    else:
        new_line = line.replace('R', '3')
    new_line = new_line[::-1]
    new_line = new_line.replace('\n', ',')
    fo2.write(new_line)
    lines += 1
fo.close()
fo2.close()
print(lines)