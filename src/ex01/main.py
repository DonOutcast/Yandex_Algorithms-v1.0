t_room, t_cond = map(int, input().split())
mode_cond = input()

if mode_cond == 'freeze' and t_room > t_cond:
    print(t_cond)
elif mode_cond == 'heat' and t_room < t_cond:
    print(t_cond)
elif mode_cond == 'auto':
    print(t_cond)
else:
    print(t_room)
