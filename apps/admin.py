from django.contrib import admin
from unfold.admin import ModelAdmin
from unfold.paginator import InfinitePaginator

from apps.models import (
    Branch,
    Company,
    Customer,
    Product,
    Sale,
)


@admin.register(Company)
class CompanyAdmin(ModelAdmin):
    list_display = ("name", "code")
    search_fields = ("name",)


@admin.register(Branch)
class BranchAdmin(ModelAdmin):
    list_display = ("name", "company__name", "location", "is_active")
    search_fields = ("name", "company__name")
    list_filter = ("company",)


@admin.register(Customer)
class CustomerAdmin(ModelAdmin):
    list_display = ("name", "company__name", "phone")
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    paginator = InfinitePaginator
    show_full_result_count = False

    list_display = (
        "name",
        "category",
        "purchase_price",
        "selling_price",
        "stock",
        "reorder_level",
        "is_active",
    )

    search_fields = ("name",)

@admin.register(Sale)
class SaleAdmin(ModelAdmin):
    list_display = ("customer__name", "product__name", "quantity", "unit_price", "discount")
    search_fields = ("customer__name", "product__name")
