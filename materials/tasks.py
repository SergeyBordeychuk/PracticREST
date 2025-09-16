import datetime

from users.models import CustomUser


def check_activ():
    for user in CustomUser.objects.all():
        time = datetime.date.today()
        if int(user.last_login[5:7]) < time.month:
            if int(user.last_login[8:10]) < time.day:
                user.is_active = False
