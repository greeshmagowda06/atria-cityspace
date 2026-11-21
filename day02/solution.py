
class OrderNotFoundError(Exception):
    pass


def lookup_order(orders, order_id):
    if not isinstance(order_id, str) or not order_id.strip():
        raise ValueError("order_id must be a non-empty string")

    for order in orders:
        if order["order_id"] == order_id:
            return order

    raise OrderNotFoundError(f"Order {order_id} not found")


def describe_order(orders, order_id):
    try:
        order = lookup_order(orders, order_id)
        return (
            f"{order['status']} order {order_id} "
            f"totaling {order['total']}"
        )
    except OrderNotFoundError:
        return f"Order {order_id} not found"


def raises_not_found(orders, order_id):
    try:
        lookup_order(orders, order_id)
        return False
    except OrderNotFoundError:
        return True
