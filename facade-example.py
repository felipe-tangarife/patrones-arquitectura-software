import uuid

class Order:
    """
    Example subsystem #1
    """
    def create(self) -> uuid:
        return str(uuid.uuid1())


class Payment:
    """
    Example subsystem #2
    """
    def verify_details(self, order_id) -> str:
        return "Payment details are ok for order " + order_id


class Shipment:
    """
    Example subsystem #2
    """
    def send(self, order_id) -> str:
        return "Shipment send process start successfully to order: " + order_id


class Notification:
    """
    Example subsystem #2
    """
    def notify(self, order_id) -> str:
        return "Generating notification to order: " + order_id


class OrderFacade:
    def __init__(self) -> None:
        self.order_system = Order()
        self.payment_system = Payment()
        self.shipment_system = Shipment()
        self.notification_system = Notification()

    def operation(self) -> str:
        print("Facade initializes subsystems")
        order_id = self.order_system.create()

        payment_response = self.payment_system.verify_details(order_id)
        shipment_response = self.shipment_system.send(order_id)
        notification_response = self.notification_system.notify(order_id)
        return "Order:" + order_id + "\n" + payment_response + "\n" + shipment_response + "\n" + notification_response


def client_code(facade: OrderFacade) -> None:
    print(facade.operation(), end="")


if __name__ == "__main__":
    facade = OrderFacade()
    client_code(facade)
