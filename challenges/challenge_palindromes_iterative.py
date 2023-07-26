def is_palindrome_iterative(word):
    if not word:
        return False
    start_index = 0
    end_index = -1
    is_palindrome = False
    for _ in range(0, len(word)):
        if word[start_index] == word[end_index]:
            start_index += 1
            end_index -= 1
            is_palindrome = True
        else:
            is_palindrome = False
            break
    return is_palindrome


if __name__ == "__main__":
    palindrome1 = "asa"
    palindrome2 = "SOCOS"
    non_palindrome1 = "pedro"
    non_palindrome2 = "agua"
    print(is_palindrome_iterative(palindrome1))
    print(is_palindrome_iterative(non_palindrome1))
    print(is_palindrome_iterative(non_palindrome2))
    print(is_palindrome_iterative(palindrome2))
