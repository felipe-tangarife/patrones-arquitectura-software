from abc import ABC, abstractmethod

class Strategy(ABC):
    """
    The Strategy interface
    """
    @abstractmethod
    def pay(self, amount):
        pass


class CreditStrategy(Strategy):
    def pay(self, amount) -> str:
        total = amount + (amount * 10 / 100)
        return "Total charged is " + str(total)


class DebitStrategy(Strategy):
    def pay(self, amount) -> str:
        total = amount + 2000
        return "Total charged is " + str(total)


class CashStrategy(Strategy):
    def pay(self, amount) -> str:
        return "Total charged is " + str(amount)


class CustomerContext():
    """
    The Context defines the interface of interest to clients.
    """

    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def pay(self, amount):
        response = self.strategy.pay(amount)
        print(response)


if __name__ == "__main__":
    context = CustomerContext(CreditStrategy())
    print("Strategy is credit pay.")
    context.pay(5000)
    print()

    print("Strategy is cash pay")
    context.strategy = CashStrategy()
    context.pay(5000)
    print()

    print("Strategy is debit pay.")
    context.strategy = DebitStrategy()
    context.pay(5000)
