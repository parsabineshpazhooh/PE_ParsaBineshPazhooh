products = {'laptop': 1200, 'phone': 800, "tablet": 500, "headphone": 150, "mouse": 50}
expensive = [i for i in products.values() if i > 500]
most_expensive = max(products.values())
cheapest = min(products.values())
average = int(sum(products.values()) / len(products.values()))
all_cost = sum(products.values())
print(f'The most expensive product is: {most_expensive}')
print(f'The cheapest product is: {cheapest}')
print(f'The average cost is {average}')
print(f'The cost is {all_cost}')
print(f'The expensive products are: {expensive}')

