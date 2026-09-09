suspect_words = ["hack", "fraud", "scam", "password", "atack"]
text = input("Enter your string: ")
words = text.split()
counter = 0
for sw in suspect_words:
    for w in words:
        if w == sw:
            counter += 1
    if counter > 0:
        print(sw, '->', counter)
