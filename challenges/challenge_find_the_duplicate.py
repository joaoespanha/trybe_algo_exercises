def find_duplicate(nums):
    if (
        not nums
        or not all(isinstance(num, int) for num in nums)
        or any(num < 0 for num in nums)
        or len(nums) == len(set(nums))
    ):
        return False
    sorted_arry = sorted(nums)

    for index in range(0, len(sorted_arry)):
        if sorted_arry[index] == sorted_arry[index + 1]:
            return sorted_arry[index]


if __name__ == "__main__":
    arry = [3, 1, 2, 4, 6, 5, 7, 7, 7, 8]

    print(find_duplicate(arry))
