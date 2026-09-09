import string
s = input("Enter string:")
letters, upper, lower, digits, spaces, special = 0, 0, 0, 0, 0, 0
for ch in s:
    if ch in string.ascii_letters:
        letters += 1
        if ch in string.ascii_uppercase:
            upper += 1
        elif ch in string.ascii_lowercase:
            lower += 1
    elif ch in string.digits:
        digits += 1
    elif ch in string.whitespace:
        spaces += 1
    else:
        special += 1

print("Letters:", letters)
print("Uppercase:", upper)
print("Lowercase:", lower)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special:", special)
