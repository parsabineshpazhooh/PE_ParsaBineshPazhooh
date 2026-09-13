products = {
    "P01": ("Laptop", 1200, 5),
    "P02": ("Phone", 800, 0),
    "P03": ("Tablet", 500, 12),
    "P04": ("Mouse", 50, 25),
    "P05": ("Keyboard", 100, 0)
}
Available, n_Available = [], []
Laptop, Phone, Tablet, Mouse, Keyboard = 0, 0, 0, 0, 0
for name, price, stock in products.values():
    if stock == 0:
        n_Available.append(name)
    elif stock > 0:
        Available.append(name)
    if name == "Laptop":
        Laptop = price * stock
    if name == "Phone":
        Phone = price * stock
    if name == "Tablet":
        Tablet = price * stock
    if name == "Mouse":
        Mouse = price * stock
    if name == "Keyboard":
        Keyboard = price * stock
all_cost = Laptop + Phone + Tablet + Mouse + Keyboard
Expensive = max(Laptop, Phone, Tablet, Mouse, Keyboard)
print(f"The most expensive : {Expensive}")
print('*' * 10)
print(f"The cost of all products : {all_cost}")
print('*' * 10)
print(f"They are Available : {Available}")
print(f"They are not Available : {n_Available}")
print('*' * 10)
print(f"Tablet : {Tablet}\nPhone : {Phone}\nMouse : {Mouse}\nKeyboard : {Keyboard}\nLaptop : {Laptop}")