# Generated by Django 5.1 on 2024-08-18 03:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.EmailField(max_length=254)),
                ('task', models.CharField(max_length=200)),
                ('due_by', models.DateTimeField()),
                ('priority', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)])),
                ('is_urgent', models.BooleanField(default=False)),
            ],
        ),
    ]
