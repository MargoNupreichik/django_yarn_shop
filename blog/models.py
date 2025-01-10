from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


# Create your models here.
class Category(models.Model):
    title = models.CharField('Название', max_length=100)
    available = models.BooleanField('Категория доступна для просмотра',
                                    default=False)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField('Название', max_length=200)
    content = models.TextField('Содержание')
    author = models.ForeignKey(User, null=True,
                               on_delete=models.SET_NULL,
                               verbose_name='Автор')
    category = models.ForeignKey(Category, null=True,
                                 on_delete=models.SET_NULL,
                                 verbose_name='Категория')

    pub_date = models.DateTimeField('Дата публикации')
    is_on_page = models.BooleanField('Запись доступна для просмотра',
                                     default=False)
    slug = models.SlugField('Слаг', max_length=200, unique=True)
    image = models.ImageField('Фото', blank=True, upload_to='blog')

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'Новости'
        ordering = ['-pub_date']

    def __str__(self):
        return self.title
