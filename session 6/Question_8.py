users = [
    ("Ali", 25, "Python"),
    ("Sara", 30, "Java"),
    ("Reza", 22, "Python"),
    ("Mina", 28, "C++"),
    ("John", 35, "Python"),
    ("David", 30, "Java"),
]
# {'python': ['Ali', 'Reza', 'John'] | 'Java': ['Sara', 'David'] | 'C++': ['Mina']}
Python, Java, C_plus = [], [], []
avg_Python, avg_Java, avg_C_plus = 0, 0, 0
Ali, Sara, Reza, Mina, John, David = 0, 0, 0, 0, 0, 0
ordering = {'python': Python, 'Java': Java, 'C++': C_plus}
for user, age, language in users:
    if language == "Python":
        Python.append(user)
        avg_Python += age
    if language == "Java":
        Java.append(user)
        avg_Java += age
    if language == "C++":
        C_plus.append(user)
        avg_C_plus += age
    if user == "David":
        David += age
    if user == "Reza":
        Reza += age
    if user == "Mina":
        Mina += age
    if user == "John":
        John += age
    if user == "Sara":
        Sara += age
    if user == "Ali":
        Ali += age




