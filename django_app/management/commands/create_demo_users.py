import random
import string
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()

class Command(BaseCommand):
    help = 'Create demo users with random passwords'

    def handle(self, *args, **kwargs):
        for _ in range(100):
            username = self.generate_random_username()
            password = self.generate_random_password()
            email = f"{username}@example.com"
            User.objects.create_user(username=username, password=password, email=email)
            self.stdout.write(self.style.SUCCESS(f"Created user: {username}"))

    def generate_random_username(self):
        return ''.join(random.choices(string.ascii_letters, k=8))

    def generate_random_password(self):
        password_characters = string.ascii_letters + string.digits + "@/./+/-/_"
        return ''.join(random.choices(password_characters, k=8))
