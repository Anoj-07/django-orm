from django.core.management.base import BaseCommand
from apps.models import Company, Customer


class Command(BaseCommand):
    help = "Create ~35 sample customers across companies"

    # handle is for logic
    def handle(self, *args, **kwargs):

        companies = Company.objects.in_bulk(
            ["SAM001", "APLE001", "GOGLE001"],
            field_name="code",
        )

        # Each tuple: (company_code, name, phone)
        customer_data = [
            ("SAM001", "Rajesh Shrestha", "9841023456"),
            ("SAM001", "Sita Gurung", "9812345678"),
            ("SAM001", "Bikash Thapa", "9851234567"),
            ("SAM001", "Anita Rai", "9803456789"),
            ("SAM001", "Prakash Adhikari", "9861234567"),
            ("SAM001", "Sunita Karki", "9814567890"),
            ("SAM001", "Dipesh Magar", "9823456780"),
            ("SAM001", "Kabita Tamang", "9845678901"),
            ("SAM001", "Nabin Poudel", "9856789012"),
            ("SAM001", "Puja Basnet", "9867890123"),
            ("SAM001", "Suresh Bhandari", "9878901234"),
            ("SAM001", "Manisha Khadka", "9889012345"),
            ("APLE001", "Rojan Shakya", "9841122334"),
            ("APLE001", "Sarita Maharjan", "9812233445"),
            ("APLE001", "Amit Joshi", "9851122333"),
            ("APLE001", "Nisha Lama", "9803344556"),
            ("APLE001", "Bijay Chettri", "9861122334"),
            ("APLE001", "Roshani Sapkota", "9814455667"),
            ("APLE001", "Kiran Dhakal", "9823344556"),
            ("APLE001", "Sabina Neupane", "9845566778"),
            ("APLE001", "Deepak Pandey", "9856677889"),
            ("APLE001", "Anjali Regmi", "9867788990"),
            ("APLE001", "Yubraj Acharya", "9878899001"),
            ("GOGLE001", "Sandeep Limbu", "9841987654"),
            ("GOGLE001", "Muna Rana", "9812876543"),
            ("GOGLE001", "Ramesh Bhattarai", "9851765432"),
            ("GOGLE001", "Kalpana Sunar", "9803654321"),
            ("GOGLE001", "Ganesh Bista", "9861543210"),
            ("GOGLE001", "Rekha Subedi", "9814432109"),
            ("GOGLE001", "Hari Oli", "9823321098"),
            ("GOGLE001", "Sharmila Khatri", "9845210987"),
            ("GOGLE001", "Tej Bahadur Rokaya", "9856109876"),
            ("GOGLE001", "Laxmi Devkota", "9867098765"),
            ("GOGLE001", "Nirmal Bam", "9878987654"),
            ("GOGLE001", "Binita Rimal", "9889876543"),
        ]

        customers = [
            Customer(
                company=companies[code],
                name=name,
                phone=phone,
            )
            for code, name, phone in customer_data
        ]

        Customer.objects.bulk_create(customers)

        self.stdout.write(
            self.style.SUCCESS(f"{len(customers)} customer created successfully.")
        )
