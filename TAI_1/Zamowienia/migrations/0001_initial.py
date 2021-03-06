# Generated by Django 4.0.4 on 2022-06-10 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Restauracja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=50)),
                ('logo', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Jedzenie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=40)),
                ('cena', models.DecimalField(decimal_places=2, max_digits=5)),
                ('obraz', models.TextField()),
                ('idRestauracji', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Zamowienia.restauracja')),
                ('kategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Zamowienia.kategoria')),
            ],
        ),
    ]
