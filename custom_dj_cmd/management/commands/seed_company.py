from django.core.management.base import BaseCommand
from apps.models import Company


class Command(BaseCommand):
    help = "Create sample products"

    # handle is for logic
    def handle(self, *args, **kwargs):
        company = [
            Company(name="Samsung", code="SAM001"),
            Company(name="Apple", code="APLE001"),
            Company(name="Google", code="GOGLE001"),
        ]

        Company.objects.bulk_create(company)

        self.stdout.write(
            self.style.SUCCESS(f"{len(company)} products created successfully.")
        )
