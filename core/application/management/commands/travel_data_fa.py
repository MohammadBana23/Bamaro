from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
from application.models import Travel
from random import choice

class Command(BaseCommand):
    
    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.fake = Faker("fa_IR")
    
    def add_arguments(self, parser):
        parser.add_argument(
            "-n", "--number", type=int, help="The number of travel to create"
        )

    def handle(self, *args, **options):
        number = options["number"] or 10
        
        success_count = 0
        failed_count = 0
        for _ in range(number):
            try:
                Travel.objects.create(
                    title = self.fake.country(),
                    content = self.fake.text(max_nb_chars=100),
                    price = self.fake.random_number(digits=2),
                    image = f'country/download{choice([1,2,3,4,5,6])}.jpeg',
                    created_at = timezone.now(),
                    updated_at = timezone.now(),
                )
                success_count += 1
            except Exception as e:
                print(e)
                failed_count += 1
        self.stdout.write(self.style.SUCCESS("=================================================="))
        self.stdout.write(self.style.SUCCESS("Travel Faker Tasks Completed!"))
        self.stdout.write(self.style.SUCCESS(f"Total Records: {failed_count+success_count}"))
        self.stdout.write(self.style.ERROR(f"Failed Records: {failed_count}"))
        self.stdout.write(self.style.WARNING(f"Success Records: {success_count}"))
