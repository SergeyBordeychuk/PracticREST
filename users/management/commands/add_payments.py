from django.core.management.base import BaseCommand
from materials.models import Course, Lesson
from users.models import CustomUser, Payment

class Command(BaseCommand):
    help = 'Add payment to the database'

    def handle(self, *args, **options):
        user, _ = CustomUser.objects.get_or_create(username='sepega', email='twnue2020@gmail.com', password='12345678qsc')
        course1, _ = Course.objects.get_or_create(name_course='skypro', description='good course for programmer')
        course2, _ = Course.objects.get_or_create(name_course='skillfactory', description='another course for programmer')

        lesson1, _ = Lesson.objects.get_or_create(name_lesson='Beginning', description='lesson for beginners', course=course1)
        lesson2, _ = Lesson.objects.get_or_create(name_lesson='Middle', description='lesson for middles', course=course2)
        lesson3, _ = Lesson.objects.get_or_create(name_lesson='Senior', description='lesson for seniors', course=course1)

        payments = [
            {'user': user, 'payment_course': course1, 'sum': 150000, 'method_payment': 'Transfer to account'},
            {'user': user, 'payment_course': course2, 'sum': 200000, 'method_payment': 'Transfer to account'},
            {'user': user, 'payment_lesson': lesson3, 'sum': 10000, 'method_payment': 'Cash'},
        ]

        for payment_data in payments:
            payment, created = Payment.objects.get_or_create(**payment_data)
            if created:
                self.stdout.write(self.style.SUCCESS(
                    f'Successfully added payment: {payment.payment_course} {payment.payment_lesson if payment.payment_lesson else None}'))
            else:
                self.stdout.write(self.style.WARNING(
                    f'Payment already exist: {payment.payment_course} {payment.payment_lesson if payment.payment_lesson else None}'))

