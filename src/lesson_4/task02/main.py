def countbeatingrooks(rook_coords):
    def add_rook(row_col, key):
        if key not in row_col:
            row_col[key] = 0
        else:
            row_col[key] += 1

    def count_pairs(rowor_col):
        pairs = 0
        for key in rowor_col:
            pairs += rowor_col[key]
        return pairs

    rook_sinrow = {}
    rook_sincol = {}
    
    for row, col in rook_coords:
        add_rook(rook_sinrow, row)
        add_rook(rook_sincol, col)
    return count_pairs(rook_sinrow) + count_pairs(rook_sincol)


        

if __name__ == "__main__":
    print(countbeatingrooks([(1, 1) ,(1, 2), (2, 1), (3, 3)]))

