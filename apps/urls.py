from django.urls import path
from apps.views import ProductView

urlpatterns = [path("products/", ProductView.as_view(), name="products-get")]
