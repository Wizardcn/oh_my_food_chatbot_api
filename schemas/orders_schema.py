def order_serializer(order) -> dict:
    return {
        "order_id": str(order["_id"]),
        "customer_id": str(order["customer_id"]),
        "display_name": str(order["display_name"]),
        "timestamp": str(order["timestamp"]),
        "cart": list(order["cart"])
    }
    
def orders_serializer(orders) -> list:
    return [order_serializer(order) for order in orders]