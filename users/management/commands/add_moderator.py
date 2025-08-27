from django.core.management.base import BaseCommand
from users.models import CustomUser

class Command(BaseCommand):

    def handle(self, *args, **options):
        user = CustomUser.objects.create(email='random@gmail.com', password='123qwe', groups='Модератор')
        user.save()
