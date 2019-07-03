from django.db import models

from phonenumber_field import modelfields

from .validators import validate_powerpoint_file,\
    validate_archived_file


class Team(models.Model):
    app_title = models.CharField(max_length=50, verbose_name='عنوان طرح')
    phone_number = modelfields.PhoneNumberField(error_messages={
                                                    'invalid': 'شماره موبایل صحیح نیست'
                                                               '\nلطفا به فرمت 0913******* وارد کنید'
                                                 },
                                                verbose_name='شماره موبایل')
    email = models.EmailField(verbose_name='ایمیل')
    app_file = models.FileField(upload_to='apps/%Y/%m', verbose_name='فایل اپلیکیشن',
                                validators=[validate_archived_file])
    powerpoint_file = models.FileField(upload_to='powerpoints/%Y/%m', verbose_name='فایل ارائه',
                                       validators=[validate_powerpoint_file])

    def __str__(self):
        return self.app_title


class TeamMember(models.Model):
    full_name = models.CharField(max_length=30, verbose_name='نام و نام خانوادگی')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name='تیم')

    def __str__(self):
        return self.full_name
