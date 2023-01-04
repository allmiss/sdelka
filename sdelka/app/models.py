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
    number = models.CharField(max_length=12, null=True)

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'


class BonusCertificate(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    category = models.CharField(max_length=20)
    discount_percent = models.CharField(max_length=4)
    picture = models.ImageField(upload_to='media/bonus', blank=True)

    class Meta:
        verbose_name = 'Бонусный сертификат'
        verbose_name_plural = 'Бонусные сертификаты'


class BuilderPartner(models.Model):
    picture = models.ImageField(upload_to='media/partners/builder', blank=True)

    class Meta:
        verbose_name = 'Застройщик'
        verbose_name_plural = 'Застройщики'


class StateOrganPartner(models.Model):
    picture = models.ImageField(upload_to='media/partners/state_organ', blank=True)

    class Meta:
        verbose_name = 'Гос. орган'
        verbose_name_plural = 'Гос. органы'

class BankPartner(models.Model):
    picture = models.ImageField(upload_to='media/partners/bank', blank=True)

    class Meta:
        verbose_name = 'Банк'
        verbose_name_plural = 'Банки'

class Estate(models.Model):
    name = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='media/estates', blank=True)
    price = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Недвижимость'
        verbose_name_plural = 'Недвижимости'