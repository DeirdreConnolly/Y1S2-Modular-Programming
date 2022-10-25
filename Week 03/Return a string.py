def longest_string(string1, string2):

    if len(string1) > len(string2):
        result = string1

    elif len(string2) > len(string1):
        result = string2

    else:
        print("null")

    return result

full_name = longest_string("abcd", "efg")
print(full_name)

print(longest_string("ab", "efg"))