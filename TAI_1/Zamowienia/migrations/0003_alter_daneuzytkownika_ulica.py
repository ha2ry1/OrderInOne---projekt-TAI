# Generated by Django 4.0.4 on 2022-06-23 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Zamowienia', '0002_daneuzytkownika_zamowienia_pozycjazamowienia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daneuzytkownika',
            name='ulica',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
