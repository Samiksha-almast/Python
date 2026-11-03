def analyse(orders):
    revenue = {}
    for order in orders:
        if order['status'] != 'CANCELLED':
            customer = order['customer']
            for item in order['items']:
                quantity = item[1]
                price = item[2]
                amount = quantity * price
                revenue[customer] = (
                    revenue.get(customer, 0) + amount
                )
    
    product_count = {}
    for order in orders:
        if order['status'] != 'CANCELLED':
            for item in order['items']:
                name = item[0]
                quantity = item[1]
                product_count[name] = (
                    product_count.get(name, 0) + quantity
                )
    sorted_products = sorted(
        product_count.items(),
        key=lambda x: (-x[1], x[0])
    )
    top_products = sorted_products[:2]
    
    customers = {order['customer'] for order in orders}
    fully_delivered = []
    for customer in customers:
        if all(
            order['status'] == 'DELIVERED'
            for order in orders
            if order['customer'] == customer
        ):
            fully_delivered.append(customer)
    fully_delivered.sort()
    
    return {
        'revenue': revenue,
        'top_products': top_products,
        'fully_delivered': fully_delivered
    }
orders = [
 {
 'id': 101,
'customer': 'Asha',
'status': 'DELIVERED',
'items': [('keyboard', 2, 1499.0), ('mouse', 1, 599.0)]
 },
 {
 'id': 102,
 'customer': 'Ravi',
 'status': 'CANCELLED',
 'items': [('monitor', 1, 10999.0)]
 },
 {
 'id': 103,
 'customer': 'Asha',
 'status': 'DELIVERED',
 'items': [('cable', 5, 199.0)]
 },
 {
 'id': 104,
 'customer': 'Meera',
 'status': 'SHIPPED',
 'items': [('keyboard', 1, 1499.0), ('monitor', 1, 10999.0)]
 },
 {
 'id': 105,
 'customer': 'Ravi',
 'status': 'DELIVERED',
 'items': [('mouse', 3, 599.0)]
 }
]
result = analyse(orders)
print(result)