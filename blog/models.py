from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from ckeditor.fields import RichTextField

# https://docs.djangoproject.com/en/4.0/topics/db/models/

# модель поста
class Post(models.Model):

    """
    class - поддерживает методы,
    модель содержит поля. https://django.fun/docs/django/ru/4.0/ref/forms/fields/
    справочник типов полей. https://django.fun/docs/django/ru/4.0/ref/models/fields/#django.db.models.SlugField
    Поля имеют настройки поведения.


    https://django-taggit.readthedocs.io/en/latest/ добавление тегов
    """

    #  мета опции
    class Meta:
        verbose_name = 'Создать пост'
        verbose_name_plural = 'Создать посты'

    title = models.CharField(max_length=200,db_index=True, help_text='не более 200 символов', verbose_name='Заголовок')
    #content = models.TextField(max_length=5000, blank=True, null=True, help_text='не более 5000 символов')
    content = RichTextField(max_length=5000, blank=True, null=True, help_text='не более 5000 символов', verbose_name='Описание')
    date_created = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    data_updated = models.DateTimeField(auto_now=True, verbose_name='Дата ообновления')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    # в url при использовании slug обязательно добавлять id + get_absolute_url()
    slug = models.SlugField(max_length=50,db_index=True, verbose_name='URL')
    likes = models.ManyToManyField(User, related_name='postcomment', blank=True, verbose_name='Понравилось')
    reply = models.ForeignKey('self', null=True, blank=True, related_name='reply_ok', on_delete=models.CASCADE, verbose_name='категории')
    download = models.ImageField(upload_to='home/alex/Рабочий стол/', verbose_name='Загрузить фото')

    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'post_slug': self.slug})

    # методы модели
    def __str__(self):
        return self.title
