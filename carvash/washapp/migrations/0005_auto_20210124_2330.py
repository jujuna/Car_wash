# Generated by Django 3.1.4 on 2021-01-24 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('washapp', '0004_hirecompany_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hirecompany',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
