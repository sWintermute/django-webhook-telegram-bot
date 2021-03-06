# Generated by Django 3.2.7 on 2021-09-20 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата')),
                ('title', models.CharField(max_length=128, verbose_name='Заголовок')),
                ('body', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name_plural': 'Список значимых события',
                'ordering': ['date'],
            },
        ),
    ]
