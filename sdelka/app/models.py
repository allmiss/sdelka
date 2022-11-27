from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    picture = models.ImageField(upload_to='media/blogs', blank=True)

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'

class People(models.Model):
    name = models.CharField(max_length=255)
    about = models.TextField()
    picture = models.ImageField(upload_to='media/people', blank=True)
    position = models.CharField(max_length=255)
    birthday = models.CharField(max_length=255)
    whatsapp_number = models.CharField(max_length=12, null=True)

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'

