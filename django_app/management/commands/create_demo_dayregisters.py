import random
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.utils import timezone
from django_app.models import dayregister  # your_app に dayregister モデルが含まれていると仮定します

User = get_user_model()

class Command(BaseCommand):
    help = 'Create demo dayregisters'

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        start_date = timezone.datetime(2023, 9, 1)  # 開始日
        end_date = timezone.datetime(2023, 9, 30)  # 終了日

        for user in users:
            date_1 = self.generate_random_date(start_date, end_date)
            date_2 = self.generate_random_date(start_date, end_date)
            date_3 = self.generate_random_date(start_date, end_date)
            amount = random.randint(1, 10000)  # ランダムな amount を生成

            dayregister.objects.create(
                user=user,
                date_1=date_1,
                date_2=date_2,
                date_3=date_3,
                amount=amount,
            )

            # データを表示
            message = (
                f"Created dayregister for user {user.username} - "
                f"date_1: {date_1}, date_2: {date_2}, date_3: {date_3}, amount: {amount}"
            )
            self.stdout.write(self.style.SUCCESS(message))

    def generate_random_date(self, start_date, end_date):
        # 指定された範囲内のランダムな日付を生成
        time_difference = end_date - start_date
        random_days = random.randint(0, time_difference.days)
        random_date = start_date + timezone.timedelta(days=random_days)
        return random_date
