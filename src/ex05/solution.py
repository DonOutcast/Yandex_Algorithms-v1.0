number = int(input())

friends = []
answer = [(-1, -1) for _ in range(number)]

for i in range(number):
    first, last = map(int, input().split())
    friends.append((first, last, i))

friends.sort()

current_start = 0
current_end = 0
current_index = -1
answer = {}

for friend in friends:
    if friend[1] > current_end:
        if current_index != -1:
            answer[current_index] = (current_start, min(friend[0], current_end))
        current_start, current_end, current_index = friend

for i in range(number):
    print(answer[i][0], answer[i][1])

