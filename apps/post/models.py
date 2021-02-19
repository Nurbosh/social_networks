from django.db import models


class Posts(models.Model):
    user = models.ForeignKey('account.CustomUsers', models.CASCADE, related_name='user_names')
    post_file = models.FileField('Пост', upload_to='post_file/')
    post_description = models.TextField('Описание')
    date_created = models.DateTimeField('дата создания', auto_now_add=True)
    like = models.PositiveSmallIntegerField('Лайки', default=0)
    comment = models.PositiveSmallIntegerField('Коментарии', default=0)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'



