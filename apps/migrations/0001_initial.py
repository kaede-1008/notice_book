# Generated by Django 2.0.4 on 2018-05-05 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=255)),
                ('book_auther', models.CharField(max_length=255)),
                ('book_illust', models.CharField(max_length=255)),
                ('publish_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
