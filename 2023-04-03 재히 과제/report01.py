class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_price(self):
        return self.price * self.quantity

    def __str__(self):
        shopping = f'{self.name:30}\t{self.quantity:6}개\t{"{:,}".format(self.price)}'
        return shopping

class ShoppingCart:
    def __init__(self):
        self.shop_list=[]

    def add(self, Product):
        self.shop_list.append(Product)

    def delete(self, Product, qty):
        Product.quantity -= qty
        if Product.quantity == 0:
            self.shop_list.remove(Product)

    def total_price(self):
        total = 0
        for i in self.shop_list:
            total += i.get_price()
        return total

    def billing(self):
        bill = f'구입 품목:\n\n'
        for i in self.shop_list:
            bill += f'{i}\n'
        bill += '-----'*13
        bill += f'\n합계' + ' '*52 + "{:,}".format(self.total_price())
        print(bill) #출력하는 기능
        return bill #다이어그램에 str return을 위함


if __name__ == '__main__':
    no1 = Product('제주 삼다수 그린 2L', 1200, 5)
    no2 = Product('신라면(120g*5입)', 4100, 2)
    no3 = Product('CJ 햇반(210g*12입)', 13980, 1)
    no4 = Product('몽쉘크림(12입)', 4780, 1)
    cart = ShoppingCart()
    cart.add(no1)
    cart.add(no2)
    cart.add(no3)
    cart.add(no4)

    cart.delete(no4, 1)
    no5 = Product('해태 구운감자(135g*5입)', 3580, 2)
    cart.add(no5)

    cart.billing()
