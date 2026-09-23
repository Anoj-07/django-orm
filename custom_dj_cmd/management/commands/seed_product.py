from django.core.management.base import BaseCommand
from apps.models import Company, Product


class Command(BaseCommand):
    help = "Create ~100 sample products across Samsung, Apple, and Google"

    # handle is for logic
    def handle(self, *args, **kwargs):

        companies = Company.objects.in_bulk(
            ["SAM001", "APLE001", "GOGLE001"],
            field_name="code",
        )

        # Each tuple: (company_code, name, category, purchase_price, selling_price, stock, reorder_level)
        product_data = [
            # ------------------ SAMSUNG ------------------
            ("SAM001", "Samsung S26 Ultra", "MOBILE", 175000, 205000, 5, 6),
            ("SAM001", "Samsung S26 Plus", "MOBILE", 160000, 190000, 5, 6),
            ("SAM001", "Samsung S25 Ultra", "MOBILE", 150000, 178000, 4, 6),
            ("SAM001", "Samsung S25 Plus", "MOBILE", 135000, 160000, 4, 6),
            ("SAM001", "Samsung Z Fold 6", "MOBILE", 250000, 295000, 3, 4),
            ("SAM001", "Samsung Z Flip 6", "MOBILE", 175000, 205000, 3, 4),
            ("SAM001", "Samsung A56", "MOBILE", 45000, 62000, 8, 10),
            ("SAM001", "Samsung A36", "MOBILE", 35000, 48000, 8, 10),
            ("SAM001", "Samsung A16", "MOBILE", 22000, 32000, 10, 12),
            ("SAM001", "Samsung M56", "MOBILE", 42000, 58000, 6, 8),
            ("SAM001", "Samsung M36", "MOBILE", 30000, 42000, 6, 8),
            ("SAM001", "Samsung Tab S10", "TABLET", 95000, 115000, 5, 6),
            ("SAM001", "Samsung Tab S9 FE", "TABLET", 65000, 82000, 5, 6),
            ("SAM001", "Samsung Tab A9", "TABLET", 28000, 38000, 6, 8),
            ("SAM001", "Samsung Galaxy Book5", "LAPTOP", 145000, 172000, 3, 4),
            ("SAM001", "Samsung Galaxy Book5 Pro", "LAPTOP", 195000, 230000, 2, 4),
            ("SAM001", "Samsung Galaxy Watch7", "WATCH", 38000, 50000, 6, 8),
            ("SAM001", "Samsung Galaxy Watch Ultra", "WATCH", 65000, 82000, 4, 6),
            ("SAM001", "Samsung Galaxy Buds3", "ACCESSORY", 15000, 21000, 10, 12),
            ("SAM001", "Samsung Galaxy Buds3 Pro", "ACCESSORY", 22000, 29000, 10, 12),
            ("SAM001", "Samsung Neo QLED TV 55in", "ELECTRONIC", 145000, 172000, 3, 4),
            ("SAM001", "Samsung Neo QLED TV 65in", "ELECTRONIC", 195000, 230000, 3, 4),
            ("SAM001", "Samsung Crystal UHD TV 43in", "ELECTRONIC", 65000, 82000, 5, 6),
            ("SAM001", "Samsung Soundbar Q990", "ELECTRONIC", 55000, 70000, 4, 6),
            ("SAM001", "Samsung Frame TV 50in", "ELECTRONIC", 175000, 205000, 2, 4),
            ("SAM001", "Samsung Refrigerator RF28", "ELECTRONIC", 185000, 220000, 3, 4),
            (
                "SAM001",
                "Samsung Washing Machine WW90",
                "ELECTRONIC",
                95000,
                118000,
                3,
                4,
            ),
            ("SAM001", "Samsung Microwave MC28", "ELECTRONIC", 25000, 33000, 5, 6),
            ("SAM001", "Samsung Portable SSD T9", "ACCESSORY", 12000, 17000, 12, 15),
            ("SAM001", "Samsung 45W Fast Charger", "ACCESSORY", 3500, 5000, 20, 25),
            ("SAM001", "Samsung Wireless Charger Duo", "ACCESSORY", 6000, 8500, 15, 18),
            ("SAM001", "Samsung Smart Monitor M8", "ELECTRONIC", 55000, 70000, 4, 6),
            (
                "SAM001",
                "Samsung Odyssey Gaming Monitor",
                "ELECTRONIC",
                85000,
                105000,
                3,
                4,
            ),
            # ------------------ APPLE ------------------
            ("APLE001", "Iphone 18 Pro", "MOBILE", 235000, 315000, 4, 6),
            ("APLE001", "Iphone 18 Pro Max", "MOBILE", 260000, 345000, 4, 6),
            ("APLE001", "Iphone 17 Pro", "MOBILE", 205000, 270000, 4, 6),
            ("APLE001", "Iphone 17 Pro Max", "MOBILE", 225000, 295000, 4, 6),
            ("APLE001", "Iphone 16e", "MOBILE", 135000, 175000, 6, 8),
            ("APLE001", "Iphone SE 4", "MOBILE", 95000, 125000, 6, 8),
            ("APLE001", "Ipad Pro M5", "TABLET", 175000, 215000, 4, 6),
            ("APLE001", "Ipad Air M3", "TABLET", 105000, 135000, 5, 6),
            ("APLE001", "Ipad 11th Gen", "TABLET", 65000, 85000, 6, 8),
            ("APLE001", "Ipad Mini 7", "TABLET", 85000, 108000, 5, 6),
            ("APLE001", "Macbook Air M4", "LAPTOP", 195000, 235000, 4, 6),
            ("APLE001", "Macbook Pro 14 M4", "LAPTOP", 285000, 340000, 3, 4),
            ("APLE001", "Macbook Pro 16 M4", "LAPTOP", 345000, 410000, 2, 4),
            ("APLE001", "Mac Mini M4", "ELECTRONIC", 105000, 130000, 4, 6),
            ("APLE001", "Mac Studio M4 Max", "ELECTRONIC", 395000, 465000, 2, 3),
            ("APLE001", "Apple Watch Series 11", "WATCH", 75000, 95000, 5, 6),
            ("APLE001", "Apple Watch Ultra 3", "WATCH", 125000, 155000, 4, 6),
            ("APLE001", "Apple Watch SE 3", "WATCH", 42000, 55000, 6, 8),
            ("APLE001", "Airpods Pro 3", "ACCESSORY", 38000, 48000, 8, 10),
            ("APLE001", "Airpods 4", "ACCESSORY", 22000, 29000, 10, 12),
            ("APLE001", "Airpods Max", "ACCESSORY", 65000, 82000, 5, 6),
            ("APLE001", "Apple TV 4K 3rd Gen", "ELECTRONIC", 25000, 33000, 5, 6),
            ("APLE001", "Apple Pencil Pro", "ACCESSORY", 18000, 24000, 8, 10),
            ("APLE001", "Magic Keyboard", "ACCESSORY", 22000, 29000, 6, 8),
            ("APLE001", "Magsafe Charger", "ACCESSORY", 6500, 9000, 15, 18),
            ("APLE001", "Apple HomePod Mini", "ELECTRONIC", 16000, 22000, 8, 10),
            ("APLE001", "Apple Studio Display", "ELECTRONIC", 195000, 230000, 2, 4),
            ("APLE001", "Apple Pro Display XDR", "ELECTRONIC", 495000, 575000, 1, 2),
            # ------------------ GOOGLE ------------------
            ("GOGLE001", "Google Pixel 10", "MOBILE", 105000, 128000, 6, 8),
            ("GOGLE001", "Google Pixel 10 Pro", "MOBILE", 145000, 175000, 5, 6),
            ("GOGLE001", "Google Pixel 10 Pro XL", "MOBILE", 165000, 198000, 4, 6),
            ("GOGLE001", "Google Pixel 9", "MOBILE", 85000, 105000, 6, 8),
            ("GOGLE001", "Google Pixel 9 Pro", "MOBILE", 120000, 145000, 5, 6),
            ("GOGLE001", "Google Pixel Fold 2", "MOBILE", 235000, 280000, 2, 4),
            ("GOGLE001", "Google Pixel Tablet", "TABLET", 65000, 85000, 5, 6),
            ("GOGLE001", "Google Pixel Watch 3", "WATCH", 45000, 58000, 6, 8),
            ("GOGLE001", "Google Pixel Buds Pro 2", "ACCESSORY", 22000, 29000, 10, 12),
            ("GOGLE001", "Google Pixel Buds A", "ACCESSORY", 9500, 13500, 12, 15),
            ("GOGLE001", "Google Nest Hub 2nd Gen", "ELECTRONIC", 15000, 21000, 8, 10),
            ("GOGLE001", "Google Nest Hub Max", "ELECTRONIC", 28000, 37000, 6, 8),
            ("GOGLE001", "Google Nest Mini", "ELECTRONIC", 5500, 8000, 15, 18),
            ("GOGLE001", "Google Nest Audio", "ELECTRONIC", 12000, 17000, 10, 12),
            ("GOGLE001", "Google Nest Wifi Pro", "ELECTRONIC", 18000, 25000, 8, 10),
            ("GOGLE001", "Google Nest Cam Battery", "ELECTRONIC", 16000, 22000, 8, 10),
            ("GOGLE001", "Google Nest Doorbell", "ELECTRONIC", 22000, 29000, 6, 8),
            ("GOGLE001", "Google Nest Thermostat", "ELECTRONIC", 19000, 26000, 6, 8),
            ("GOGLE001", "Google Chromecast HD", "ELECTRONIC", 6500, 9500, 15, 18),
            ("GOGLE001", "Google TV Streamer 4K", "ELECTRONIC", 9500, 13500, 12, 15),
            ("GOGLE001", "Google Pixel 9a", "MOBILE", 55000, 72000, 6, 8),
            ("GOGLE001", "Google Pixel 8a", "MOBILE", 48000, 62000, 6, 8),
        ]

        products = [
            Product(
                company=companies[code],
                name=name,
                category=category,
                purchase_price=purchase_price,
                selling_price=selling_price,
                stock=stock,
                reorder_level=reorder_level,
            )
            for code, name, category, purchase_price, selling_price, stock, reorder_level in product_data
        ]

        Product.objects.bulk_create(products)

        self.stdout.write(
            self.style.SUCCESS(f"{len(products)} product created successfully.")
        )
