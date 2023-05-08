
def count_beating_queen(queen_coords):
    def add_queen(row_col, key):
        if key not in row_col:
            row_col[key] = 0
        else:
            row_col[key] += 1

    def count_pairs(rowor_col):
        pairs = 0
        for key in rowor_col:
            pairs += rowor_col[key]
        return pairs

    queen_sinrow = {}
    queen_sincol = {}
    diagonal_right = {}
    diagonal_left = {}


    for row, col in queen_coords:
        add_queen(queen_sinrow, row)
        add_queen(queen_sincol, col)
        add_queen(diagonal_right, row + col)
        add_queen(diagonal_left, row - col)
    return count_pairs(queen_sinrow) + count_pairs(queen_sincol) + \
           count_pairs(diagonal_right) + count_pairs(diagonal_left) 


        

if __name__ == "__main__":
    print(count_beating_queen([(1, 1) ,(1, 2),  ]))

