t_room, t_cond = map(int, input().split())
mode_cond = input()

print(t_cond if (mode_cond == 'freeze' and t_room > t_cond) or (
            mode_cond == 'heat' and t_room < t_cond) or mode_cond == 'auto' else t_room)
