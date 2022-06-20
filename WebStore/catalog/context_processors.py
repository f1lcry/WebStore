from .models import Category
from cart.models import Cart


def categories(request):
    names_category = Category.objects.all()
    context = {
        "categories": names_category,
    }
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user)
        context.update({
            "carts": carts,
        })

    return context
