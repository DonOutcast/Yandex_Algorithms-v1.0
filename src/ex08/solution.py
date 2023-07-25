query = input()
count = int(input())
now_path = []
for i in range(count):

    line = input()
    now_file = line.strip()
    spaces = 0
    while spaces < len(line) and line[spaces] == '':
        spaces += 1

    now_path = now_path[:spaces]
    now_path.append(now_file)
    
    if now_file == query:
        print('/'+'/'.join(now_path))
        break

