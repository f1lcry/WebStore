from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from catalog.models import Product
from django.template.loader import render_to_string
from django.views import View
from django.views.generic import DetailView

from .models import Cart
from django.shortcuts import get_object_or_404, HttpResponseRedirect


@login_required(login_url='login')
def index(request):
    # for cart in carts:
    #     cart.is_checked = True
    #     cart.save()
    return render(request, "cart/cart_info.html")


def add_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart = Cart.objects.filter(product=product, user=request.user).first()
    if not cart:
        cart = Cart(user=request.user, product=product)
    cart.total_quantity += 1
    cart.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove_product(request, pk):
    if request.is_ajax():
        pk = pk
        cart_product = Cart.objects.filter(pk=pk).first()
        cart_product.delete()
        cart = Cart.objects.filter(user=request.user).all()
        # В теории можно сделать как в методе add_product, то есть redirect, ведь
        # в индексе и так прогружается корзина
        context = {
            "carts": cart,
        }
        result = render_to_string("cart/total_cart.html", context)
        return JsonResponse({
            "result": result
        })


def edit_cart(request, pk, quantity):
    # Здесь можно просто объединить методы add_product и remove_product, так как в них выполняется по сути то же самое
    if request.is_ajax():
        quantity = quantity
        cart_product = Cart.objects.filter(pk=pk).first()
        if quantity > 0:
            cart_product.total_quantity = int(quantity)
            cart_product.save()
        else:
            cart_product.delete()
        cart = Cart.objects.filter(user=request.user).all()
        # print(request.data)
        context = {
            "carts": cart,
        }
        result = render_to_string("cart/total_cart.html", context)
        return JsonResponse({
            "result": result
        })


def check(request, is_checked):
    # придёт в str
    if request.is_ajax():
        is_checked = int(is_checked)
        pk = int(request.GET.get("cart_pk", None))
        cart_product = Cart.objects.filter(pk=pk).first()
        if is_checked:
            cart_product.is_checked = True
        else:
            cart_product.is_checked = False
        cart = Cart.objects.filter(user=request.user)
        cart_product.save()
        print(cart[0].is_checked)
        print(cart_product.total_price_to_pay())
        context = {
            "carts": cart,
        }
        result = render_to_string("cart/total_cart.html", context)
        return JsonResponse({
            "result": result
        })
    # TODO(1): 1) integrate other cart's methods
    # TODO(2): 2) checkboxes on products
