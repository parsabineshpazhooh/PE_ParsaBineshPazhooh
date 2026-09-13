inventory = {"apple": 20, "banana": 5, "orange": 0, "milk": 12, "bread": 0}
n_available = [i for i in inventory.values() if i > 0]
n_o_o_s = [i for i in inventory.values() if i > 0]
Available = []
Out_of_stock = []
for i in inventory.keys():
    if inventory[i] > 0:
        Available.append(i)
    else:
        Out_of_stock.append(i)
print(f"Availables : {Available}")
print(f"Out of stocks : {Out_of_stock}")
print(f"Number of availables : {n_available}")
print(f"Number of out of stocks : {n_o_o_s}")