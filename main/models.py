from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    def __str__(self):
        return  (self.name)


class MainPost(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=255)
    body = models.CharField(verbose_name='Текст', max_length=2000)
    image_url = models.CharField(verbose_name='URL-картинки', max_length=1023)

    def __str__(self):
        return  (self.title)

class BlogPost(models.Model):
    author_name = models.CharField(verbose_name='Автор поста', max_length=255, default='x')
    avatar = models.CharField(verbose_name='Аватар', max_length=1023, default='x')
    title = models.CharField(verbose_name='Заголовок', max_length=255)
    body = models.CharField(verbose_name='Текст', max_length=2000)
    image_url = models.CharField(verbose_name='URL-картинки', max_length=1023)

    def __str__(self):
        return  (self.title)