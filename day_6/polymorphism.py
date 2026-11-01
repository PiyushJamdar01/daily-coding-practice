class CreditCard:
    def pay(self):
        print("Payment using Credit Card")


class UPI:
    def pay(self):
        print("Payment using UPI")


class Cash:
    def pay(self):
        print("Payment using Cash")


def make_payment(method):
    method.pay()


c = CreditCard()
u = UPI()
ca = Cash()

make_payment(c)
make_payment(u)
make_payment(ca)