from django.shortcuts import render
from .models import Category, Product
from cart.models import Cart
from django.http import Http404


def index(request, pk=None, tag_name=None):
    context = {}
    is_main = False

    if pk:
        # Выделять нажатую категорию
        products = Product.objects.filter(category__pk=pk).order_by("-is_available")
        category = Category.objects.get(pk=pk)
        context.update({
            "category": category
        })
    elif tag_name:
        products = Product.objects.filter(tags__name=tag_name).order_by("-is_available")
        context.update({
            "tag": tag_name
        })
    else:
        products = Product.objects.all()
        is_main = True

    basket = []
    if request.user.is_authenticated:
        basket = Cart.objects.filter(user=request.user)

    context.update({
        "is_main": is_main,
        "products": products,
        "basket": basket
    })

    print(context)
    return render(request, "catalog/catalog.html", context)


def product_info(request, name):
    try:
        product = Product.objects.get(name=name)
    except:
        raise Http404("Product not found")
    names_category = Category.objects.all()

    if product.quantity == 0:
        product.is_available = False

    context = {
        "categories": names_category,
        "product": product
    }

    return render(request, "catalog/product_info.html", context)


def add_product(request, action):
    pass


# TODO: make a very hard sql-request
# TODO: redesign
# TODO: make products, categories and tags (10+)
