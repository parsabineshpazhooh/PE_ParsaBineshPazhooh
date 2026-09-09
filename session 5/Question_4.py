s = input("Enter your string : ")
words = s.split()
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
max_word = max(counts, key=counts.get)
print(max_word, '->', counts[max_word])
