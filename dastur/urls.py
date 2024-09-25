from django.urls import path
from .views import *

urlpatterns = [
    path("", asosiy_sahifa),
    path("shop/", shop),
    path("books/", booksPage),
]
