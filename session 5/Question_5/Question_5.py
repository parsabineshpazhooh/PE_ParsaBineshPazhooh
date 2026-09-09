s = input("Enter your string: ")
words = s.split()
longest = words[0]
for w in words:
    if len(w) > len(longest):
        longest = w

print(longest)
print('Length:', len(longest))
'''
yek nokte vojood dare tooye soali ke dadid oon ham ine ke tooye mesal programming 
toolani tarine vali shome goftid excactly ke eshtebah hast.
'''