# Generated by Django 4.0.4 on 2022-05-23 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='golduser',
            name='goldWeight',
            field=models.DecimalField(blank=True, decimal_places=10, default=0, max_digits=30),
        ),
    ]
