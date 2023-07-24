l, n, m = map(int, input().split())

balance =[0] * (l + 1)

for i in range(n):
    left, right = map(int, input().split())
    balance[left - 1] += 1
    balance[right] -= 1

