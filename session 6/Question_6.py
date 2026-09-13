sales = (
    ("Ali", "Laptop", 1200),
    ("Sara", "Phone", 800),
    ("Ali", "Phone", 800),
    ("Reza", "Laptop", 1200),
    ("Sara", "Laptop", 1200),
    ("Ali", "Mouse", 50),
)
Ali, Sara, Reza = 0, 0, 0
Mouse, laptop, phone = 0, 0, 0
for customer, product, price in sales:
    if customer == "Ali":
        Ali += price
    if customer == "Sara":
        Sara += price
    if customer == "Reza":
        Reza += price
    if product == "Mouse":
        Mouse += 1
    if product == "Laptop":
        laptop += 1
    if product == "Phone":
        phone += 1
Max_buy = max(Ali, Sara, Reza)
print(f"times products sold:\n1)Mouse: {Mouse}\n2)Laptop: {laptop}\n3)Phone: {phone}")
print('*' * 15)
print(f"Costs costumers bought:\n1)Ali : {Ali}\n2)Sara : {Sara}\n3)Reza : {Reza}")
print('*' * 15)
print(f"Max buy : {Max_buy}")
print('*' * 15)
print(f"Total price earned: {Ali + Sara + Reza}")
