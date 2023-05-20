# s = input()

# def print_chart(s) -> None:
#     sym_count = {}
#     max_sym_count = 0
#     for sym in s:
#         if sym not in sym_count:
#             sym_count[sym] = 0
#         sym_count[sym] += 1
#         max_sym_count = max(max_sym_count, sym_count[sym])
#     sorted_uniq_syms = sorted(sym_count.keys())
#     for row in range(max_sym_count, 0 , -1):
#         for sym in sorted_uniq_syms:
#             if sym_count[sym] >= row:
#                 print("#", end="")
#             else:
#                 print(" ", end="")
#         print()
#     print(''.join(sorted_uniq_syms))

# print_chart(s)
from collections import Counter

def print_chart(s):
    sym_count = Counter(s)
    print(sym_count)
    max_sym_count = max(sym_count.values())
    sorted_uniq_syms = sorted(sym_count.keys())

    for row in range(max_sym_count, 0, -1):
        for sym in sorted_uniq_syms:
            print("#" if sym_count[sym] >= row else " ", end="")
        print()
    print("".join(sorted_uniq_syms))

print_chart("Hello, World!")




