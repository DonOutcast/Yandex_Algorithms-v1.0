def two_terms_with_sum_x(nums:list[int], x:int):
    prev_nums = set()
    for now_num in nums:
        if x - now_num in prev_nums:
            return now_num, x - now_num
        prev_nums.add(now_num)
    return 0, 0

if __name__ == "__main__":
    print(two_terms_with_sum_x([1, 2, 3], 5)
