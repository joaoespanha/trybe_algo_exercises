def merge_sort(word: str) -> str:
    if len(word) <= 1:
        return word
    mid = len(word) // 2

    left = merge_sort(word[:mid])
    right = merge_sort(word[mid:])

    return merge(left, right)


def merge(left: str, right: str) -> str:
    result = []
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result += left[left_index]
            left_index += 1
        else:
            result += right[right_index]
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]

    return "".join(result)


if __name__ == "__main__":
    string = "dcbaf"
    print(merge_sort(string))
