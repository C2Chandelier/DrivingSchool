from django.core.management.base import BaseCommand
from faker import Faker
from Secretary.models import Planning
from Student.models import Student
from Instructor.models import Instructor
import random
from datetime import datetime, timedelta

fake = Faker()

class Command(BaseCommand):
    help = 'Generate random planning records'

    def handle(self, *args, **options):
        students = list(Student.objects.all())
        instructors = list(Instructor.objects.all())
        
        # Generate random planning records
        for _ in range(100):
            student = random.choice(students)
            instructor = random.choice(instructors)
            date = fake.date_time_between(start_date="-1y", end_date="now")
            place = fake.city()

            planning = Planning(student=student, instructor=instructor, date=date, place=place)
            planning.save()

        self.stdout.write(self.style.SUCCESS('Successfully generated random planning records'))
