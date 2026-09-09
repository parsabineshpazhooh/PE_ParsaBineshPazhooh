sentence_1 = input("Enter first sentence: ").split(" ")
sentence_2 = input("Enter second sentence: ").split(" ")
for i in sentence_1:
    for j in sentence_2:
        if i == j:
            print(j)
