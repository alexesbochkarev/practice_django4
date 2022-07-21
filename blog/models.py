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
    модель содержит поля.
    Поля имеют настройки поведения.
    https://django-taggit.readthedocs.io/en/latest/
    """

    #  мета опции
    class Meta:
        verbose_name = 'Создать пост'
        verbose_name_plural = 'Создать посты'

    # поля модели
    title = models.CharField(max_length=200,db_index=True, help_text='не более 200 символов') # настройки полей
    #content = models.TextField(max_length=5000, blank=True, null=True, help_text='не более 5000 символов')
    content = RichTextField(max_length=5000, blank=True, null=True, help_text='не более 5000 символов')
    date_created = models.DateTimeField(default=timezone.now) # дата создания
    data_updated = models.DateTimeField(auto_now=True) # дата обновления
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # в url при использовании slug обязательно добавлять id + get_absolute_url()
    slug = models.SlugField(max_length=50)
    likes = models.ManyToManyField(User, related_name='postcomment', blank=True)
    reply = models.ForeignKey('self', null=True, related_name='reply_ok', on_delete=models.CASCADE)

    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    # методы модели
    def __str__(self):
        return self.title
