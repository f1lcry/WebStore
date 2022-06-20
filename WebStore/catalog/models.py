from django.db import models


class Category(models.Model):
    name = models.CharField("Name", max_length=50)
    description = models.TextField("Description")
    is_active = models.BooleanField("Is active", default=True)

    def __str__(self):
        return self.name

    def get_products(self):
        return Product.objects.filter(category=self.pk)[:2]

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Tag(models.Model):
    name = models.CharField("Name", max_length=50)
    description = models.TextField("Description")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"


class Product(models.Model):
    name = models.CharField("Name", max_length=50)
    description = models.TextField("Description")
    image = models.ImageField("Image", blank=True)
    price = models.DecimalField("Price", max_digits=15, decimal_places=2)
    quantity = models.IntegerField("Quantity", default=0)
    is_available = models.BooleanField("Is available", default=True)
    category = models.ForeignKey(Category, null=False, on_delete=models.CASCADE)
    date_created = models.DateField("Date created", auto_now_add=True)
    tags = models.ManyToManyField(Tag, "Tags")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def tags_product(self):
        return self.tags


# class News(models.Model):
#     title = models.CharField("Title", max_length=50)
#     content = models.TextField("Content")
#     date_published = models.DateField("Date published", auto_now_add=True)
#     product = models.ForeignKey(Product, null=False, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.title
#
#
# class Comment(models.Model):
#     title = models.CharField("Title", max_length=50)
#     user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
#     date_created = models.DateField("Date created", auto_now_add=True)
#     grade = models.IntegerField("Grade", default=None)
#     content = models.CharField("Content", max_length=200)
#
#     def __str__(self):
#         return self.title
#
#
# class Order(models.Model):
#     number = models.CharField("Order's number", max_length=30)
#     products = models.ManyToManyField(Product, "Products")
#     total_amount = models.DecimalField("Total amount", max_digits=25, decimal_places=2)
#     is_active = models.BinaryField("Status")
#     date_created = models.DateField("Date created", auto_now_add=True)
#     user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.number
