from django.core.management.base import BaseCommand
from faker import Faker
from django.contrib.auth.hashers import make_password
from Instructor.models import Instructor

fake = Faker()

class Command(BaseCommand):
    help = 'Generate random instructor records'

    def handle(self, *args, **options):
        # Function to generate a random password
        def generate_random_password():
            return make_password(fake.password())

        # Generate random student records
        for _ in range(100):
            username = fake.user_name()
            password = generate_random_password()

            instructor = Instructor(username=username, password=password)
            instructor.save()

        self.stdout.write(self.style.SUCCESS('Successfully generated random instructor records'))