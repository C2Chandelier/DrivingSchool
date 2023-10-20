from django.core.management.base import BaseCommand
from faker import Faker
from django.contrib.auth.hashers import make_password
from Student.models import Student

fake = Faker()

class Command(BaseCommand):
    help = 'Generate random student records'

    def handle(self, *args, **options):
        # Function to generate a random password
        def generate_random_password():
            return make_password(fake.password())

        # Generate random student records
        for _ in range(100):
            username = fake.user_name()
            password = generate_random_password()
            h_total = fake.random_int(0, 100)
            h_remaining = fake.random_int(0, h_total)

            student = Student(username=username, password=password, h_total=h_total, h_remaining=h_remaining)
            student.save()

        self.stdout.write(self.style.SUCCESS('Successfully generated random student records'))
