# Generated by Django 4.0.4 on 2022-06-18 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Zamowienia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DaneUzytkownika',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=15)),
                ('nazwisko', models.CharField(max_length=15)),
                ('miejscowosc', models.CharField(max_length=20)),
                ('ulica', models.CharField(max_length=60)),
                ('nrDomu', models.CharField(max_length=6)),
                ('nrMieszkania', models.IntegerField(null=True)),
                ('telefon', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Zamowienia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('klient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Zamowienia.daneuzytkownika')),
            ],
        ),
        migrations.CreateModel(
            name='PozycjaZamowienia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jedzenie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Zamowienia.jedzenie')),
                ('zamowienie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Zamowienia.zamowienia')),
            ],
        ),
    ]
