from django.db import models


class CustomUsers(models.Model):
    user_name = models.CharField('Логин', max_length=63)
    phone = models.CharField('номер', max_length=20)
    email = models.CharField('Почта', max_length=127)
    data_birth = models.DateField('Дата рождения')
    avatarka = models.FileField('Изоброжение', upload_to='avatarka_users/')
    bio = models.CharField('О себе', max_length=255)
    subscription_count = models.PositiveSmallIntegerField('Подписки', default=0)
    subscribers_count = models.PositiveSmallIntegerField('Подписчики', default=0)
    count_post = models.PositiveSmallIntegerField('Публикации', default=0)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.user_name
