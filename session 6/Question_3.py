x = input("Enter your string: ").strip()
d = {}
for i in x:
    if i.isalpha():
        i = i.lower()
        d[i] = d.get(i, 0) + 1
print(d)
