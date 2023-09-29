
from django.urls import path , include
from core.views import *
urlpatterns = [
    path("",home, name="home"),
    # path("news/",news, name="news "),
    path("contact/", contact, name="contact"),
    path("products/", products , name="products"),
    # path("search_view/", search_view , name="search_view"),
    path("product/<slug:slug>/", product_detail, name="product_detail"),
    path('search/', search, name='search'),



    # path("product_detail/<int:id/", product_detail , name="product_detail"),

]




