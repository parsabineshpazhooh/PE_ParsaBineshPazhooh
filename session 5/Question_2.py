Enter_String = input("Enter String: ")


def remover(s):
    seemed = set()
    result = ""
    for ch in s:
        if ch not in seemed:
            result += ch
            seemed.add(ch)
    print(result)


remover(Enter_String)
