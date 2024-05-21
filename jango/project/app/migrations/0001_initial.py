# Generated by Django 5.0.6 on 2024-05-20 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('phone', models.CharField(default='', max_length=10)),
                ('email', models.EmailField(default='', max_length=254)),
                ('password1', models.CharField(max_length=40)),
                ('password2', models.CharField(max_length=40)),
            ],
        ),
    ]
