# Author:       Deirdre Connolly
# Filename:     Method Functions.py
# Description:  Value-returning functions


def join_names(first_name, surname):
    result = first_name + ", " + surname
    return result

ans = join_names("Ben", "Sisko")
print(ans)
