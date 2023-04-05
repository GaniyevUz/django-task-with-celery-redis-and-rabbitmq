from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from faker import Faker


class Command(BaseCommand):
    fake = Faker()

    def handle(self, *args, **options):
        for _ in range(100):
            User.objects.create(
                username=self.fake.user_name(),
                first_name=self.fake.first_name(),
                last_name=self.fake.last_name(),
                email=self.fake.email(),
                password=make_password('1')
            )
