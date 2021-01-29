# Generated by Django 3.1.4 on 2021-01-29 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('washapp', '0005_auto_20210124_2330'),
    ]

    operations = [
        migrations.CreateModel(
            name='Washer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=40)),
                ('percentage', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='washercompany',
            name='locations',
        ),
        migrations.DeleteModel(
            name='HireCompany',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.DeleteModel(
            name='WasherCompany',
        ),
    ]
