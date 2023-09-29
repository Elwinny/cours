from django.urls import path

from core.api.views import *

urlpatterns = [
    path('products/<int:id>/' , ProductDetailApiView.as_view() , name="products-detail" ),
]