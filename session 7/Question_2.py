def process_order(customer, *products, **options):
    print('Hello', customer)
    print('products:', list(products))
    print('taxes and discount :', options)
    final_cost = 0
    for i in options.keys():
        if i == 'discount':
            final_cost -= options[i]
        elif options[i] != 'discount':
            final_cost += options[i]
    print('final cost:', final_cost)


process_order("Ali", "Laptop", "Mouse", "Keyboard", discount=10, tax=9, shipping=200000)
