from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="catalog"),
    path("category/<int:pk>", views.index, name="product_list"),
    path("product/<str:name>", views.product_info, name="product_info"),
    path("tag/<str:tag_name>", views.index, name="tags_list"),
    path("add_product/<str:action>", views.add_product, name="add_product"),
]
