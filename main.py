from abc import ABC, abstractmethod
from dataclasses import dataclass

class PricingRule(ABC):

    @abstractmethod
    def calculate_price(self, quantity: int) -> int:
        pass

@dataclass
class IndividualPrice(PricingRule):
    price: int

    def calculate_price(self, quantity: int) -> int:
        return quantity * self.price


@dataclass   
class SpecialPrice(PricingRule):
    special_price_quantity: int
    special_price: int
    normal_price: int


    def calculate_price(self, quantity: int) -> int:
        special_price_count = quantity // self.special_price_quantity
        normal_price_count = quantity % self.special_price_quantity
        return (special_price_count * self.special_price) + (normal_price_count * self.normal_price)


@dataclass
class CheckoutKata:
    pricing_rules: SpecialPrice
    cart: dict

    def scan(self, item):
        if item not in self.cart:
            self.cart[item] = 1
        else:
            self.cart[item] += 1

    def calculate_total(self):
        total_price = 0
        for item, quantity in self.cart.items():
            if item in self.pricing_rules:
                total_price += self.pricing_rules[item].calculate_price(quantity)
            else:
                total_price += quantity * self.pricing_rules[item]
        return total_price


if __name__ == "__main__":
    pricing_rules = {
        "A": SpecialPrice(special_price_quantity=3, special_price=130, normal_price=50),
        "B": SpecialPrice(special_price_quantity=2, special_price=45, normal_price=30),
        "C": IndividualPrice(price=20),
        "D": IndividualPrice(price=15)
    }

    co = CheckoutKata(pricing_rules, {})
    co.scan("A")
    co.scan("A")
    co.scan("A")
    co.scan("A")
    co.scan("B")
    co.scan("B")
    co.scan("B")
    co.scan("C")
    co.scan("D")
    print(co.calculate_total()) 