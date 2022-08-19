def cart_serializer(cart) -> dict:
    return {
        "customer_id": cart["customer_id"],
        "cart": cart["cart"]
    }
    
def carts_serializer(carts) -> list:
    return [cart_serializer(cart) for cart in carts]