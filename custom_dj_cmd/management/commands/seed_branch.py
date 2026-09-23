from django.core.management.base import BaseCommand
from apps.models import Branch, Company


class Command(BaseCommand):
    help = "Create Branch"

    # handle is for logic
    def handle(self, *args, **kwargs):

        companies = Company.objects.in_bulk(
            ["SAM001", "APLE001", "GOGLE001"],
            field_name="code",
        )

        branch = [
            Branch(
                company=companies["SAM001"],
                name="Samsung Nepal",
                location="Kathmandu",
            ),
            Branch(
                company=companies["APLE001"],
                name="Apple Nepal",
                location="Kathmandu",
            ),
            Branch(
                company=companies["GOGLE001"],
                name="Google Nepal",
                location="Kathmandu",
            ),
        ]

        Branch.objects.bulk_create(branch)

        self.stdout.write(
            self.style.SUCCESS(f"{len(branch)} branches created successfully.")
        )
