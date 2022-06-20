from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='cart'),
    path('add/<int:pk>', views.add_product, name='add_product'),
    path('remove/<int:pk>', views.remove_product, name='remove_product'),
    path('edit/<int:pk>/<int:quantity>', views.edit_cart, name='edit_cart'),
    path("check/<int:is_checked>", views.check, name="check")
]