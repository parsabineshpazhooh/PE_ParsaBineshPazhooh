orders = [
    ("Ali", "Laptop"),
    ("Sara", "Phone"),
    ("Ali", "Phone"),
    ("Reza", "Laptop"),
    ("Sara", "Laptop"),
    ("Ali", "Tablet"),
    ("Reza", "Phone"),
]
Ali_order = []
Sara_order = []
Reza_order = []
All_orders = {"Ali": Ali_order, "Sara": Sara_order, "Reza": Reza_order}
for costumers, products in orders:
    if costumers == "Ali":
        Ali_order.append(products)
    if costumers == "Sara":
        Sara_order.append(products)
    if costumers == "Reza":
        Reza_order.append(products)
print(All_orders)