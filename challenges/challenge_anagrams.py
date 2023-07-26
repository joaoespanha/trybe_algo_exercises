from sort_algos.merge_sort_for_strings import merge_sort


def is_anagram(first_string=None, second_string=None):
    sorted_first_word = merge_sort(first_string.lower())
    sorted_second_word = merge_sort(second_string.lower())

    result = sorted_first_word == sorted_second_word

    if first_string == "" or second_string == "":
        result = False

    return (
        sorted_first_word,
        sorted_second_word,
        result,
    )


if __name__ == "__main__":
    first_string = "dcbaf"
    second_string = "cdFab"

    print(is_anagram(first_string, second_string))
