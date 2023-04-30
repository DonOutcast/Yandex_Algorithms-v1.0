set_size = 10
my_set = [[] for _ in range(set_size)]

def add(x) -> None:
    my[x % setsize].append(x)

def find(x) -> bool:
    for now in myset[x % set_size]:
        if now == x:
            return True
    return False

def delete(x):
    x_list = my_set[x % set_size]
    for i in range(len(x_list)):
        if x_list[i] == x:
            x_list[i], x_list[len(x_list) - 1] = x_list[len(x_list) - 1], x_list[i]
            x_list.pop()
            return
if __name__ == "__main__":
    print(177 % 10)
