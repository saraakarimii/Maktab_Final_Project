# Generated by Django 3.2.9 on 2022-01-03 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_costumuser_device'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costumuser',
            name='device',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]