from django.db import models
from catalog.models import Product
from authentication.models import Account


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    total_quantity = models.IntegerField("Total quantity", default=0)
    date_created = models.DateField("Date created", auto_now_add=True)
    is_checked = models.BooleanField("is_cart_checked", default=True)
    user = models.ForeignKey(Account, null=False, on_delete=models.CASCADE, related_name='basket')

    def count_price(self):
        return round(self.product.price * self.total_quantity, 2)

    def total_price(self):
        carts = Cart.objects.filter(user=self.user)
        price = sum([cart.count_price() for cart in carts])
        return price

    def count_carts_quantities(self):
        carts = Cart.objects.filter(user=self.user)
        quantity = sum([cart.total_quantity for cart in carts])
        return quantity

    def total_price_to_pay(self):
        carts = Cart.objects.filter(user=self.user, is_checked=True)
        price = sum([cart.count_price() for cart in carts])
        return price

    def __str__(self):
        return self.user.first_name
