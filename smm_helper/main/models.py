from django.db import models

class Bloger(models.Model):
    title = models.TextField(max_length=100, verbose_name='Название аккаунта')
    num_of_pubs = models.IntegerField(verbose_name='Количество публикаций')
    num_of_subs = models.IntegerField(verbose_name='Количество подписчиков')
    num_of_likers = models.IntegerField(verbose_name='Количество лайков')
    prof_descr = models.TextField(max_length=250, verbose_name='Описание профиля')
    contacts = models.TextField(max_length=100, verbose_name='Контакты')
    last_pubs =  models.IntegerField(verbose_name='Количество публикаций за 30 дней')
    last_likers = models.IntegerField(verbose_name='Количество лайков за 30 дней')
    last_views = models.IntegerField(verbose_name='Количество просмотров за 30 дней')
    last_coments = models.IntegerField(verbose_name='Количество комментариев за 30 дней')
    er = models.IntegerField(verbose_name='Коеффициент вовлеченности')

    class Meta:
       verbose_name= 'Блогер'
       verbose_name_plural = 'Блогеры'