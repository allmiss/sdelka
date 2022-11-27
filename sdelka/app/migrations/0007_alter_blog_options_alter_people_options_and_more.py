# Generated by Django 4.1.3 on 2022-11-14 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_people_alter_blog_picture'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name': 'Блог', 'verbose_name_plural': 'Блоги'},
        ),
        migrations.AlterModelOptions(
            name='people',
            options={'verbose_name': 'Работник', 'verbose_name_plural': 'Работники'},
        ),
        migrations.RenameField(
            model_name='people',
            old_name='name',
            new_name='Дата рождения (xx.xx.xxxx)',
        ),
        migrations.AddField(
            model_name='people',
            name='+7xxxxxxxxxx (без пробельно)',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='people',
            name='Должность',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='people',
            name='ФИО',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]