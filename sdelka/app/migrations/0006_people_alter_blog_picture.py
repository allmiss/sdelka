# Generated by Django 4.1.3 on 2022-11-14 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_blog_img_blog_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('about', models.TextField()),
                ('picture', models.ImageField(blank=True, upload_to='media/people')),
            ],
        ),
        migrations.AlterField(
            model_name='blog',
            name='picture',
            field=models.ImageField(blank=True, upload_to='media/blogs'),
        ),
    ]