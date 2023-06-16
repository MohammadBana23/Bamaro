from django.core.management.base import BaseCommand
from application.models import CustomUser
from faker import Faker


class Command(BaseCommand):
    help = 'Create a superuser if one does not already exist'
    
    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.fake = Faker("fa_IR")
    
    def handle(self, *args, **options):
        if not CustomUser.objects.filter(is_superuser=True).exists():
            CustomUser.objects.create_superuser(
                username='admin',
                email='admin@admin.com',
                phone='091111111111',
                password='admin',
                birthdate=self.fake.date(),
            )
            for i in range(5) :
                try:
                    CustomUser.objects.create_user(username=f'username{str(i + 1)}' , password="fake@1234",
                                                    phone = self.fake.phone_number() , email = self.fake.email(),
                                                    birthdate=self.fake.date())
                except Exception as e:
                    print(e)
                    print("Username has already been taken!")

            self.stdout.write(self.style.SUCCESS('Successfully created superuser.'))
        else:
            self.stdout.write(self.style.WARNING('Superuser already exists.'))
        