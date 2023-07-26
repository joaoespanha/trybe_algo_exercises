def is_palindrome_recursive(word, low_index, high_index):
    # se passado uma string vazia como word retorna False
    if len(word) == 0:
        return False
    # se word for palindrome retorna true
    if low_index == high_index:
        return True

    elif word[low_index] == word[high_index]:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    # senao retorna false
    else:
        return False


if __name__ == "__main__":
    palindrome1 = "asa"
    palindrome2 = "SOCOS"
    non_palindrome1 = "pedro"
    non_palindrome2 = "agua"
    print(is_palindrome_recursive(palindrome1, 0, len(palindrome1) - 1))
    print(
        is_palindrome_recursive(non_palindrome1, 0, len(non_palindrome1) - 1)
    )
    print(
        is_palindrome_recursive(non_palindrome2, 0, len(non_palindrome2) - 1)
    )
    print(is_palindrome_recursive(palindrome2, 0, len(palindrome2) - 1))
