# Generated by Django 3.1.3 on 2020-11-27 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='id',
            field=models.TextField(primary_key=True, serialize=False),
        ),
    ]
