from django.db import models

# Create your models here.
# Modele wykorzystane w tworzeniu bazy danych

'''
class Platnosc(models.Model):
    order = models.IntegerField(default=1)
    amount_required = models.IntegerField(default=1)
    description = models.CharField(max_length=200, default="test")
    currency = models.CharField(max_length=3, default="PLN")
    backend = models.CharField(max_length=5, default="PayU")
'''


class Restauracja(models.Model):
    nazwa = models.CharField(max_length=50)
    logo = models.TextField()

class Kategoria(models.Model):
    nazwa = models.CharField(max_length=10)

class Jedzenie(models.Model):
    nazwa = models.CharField(max_length=40)
    idRestauracji = models.ForeignKey(Restauracja, on_delete=models.CASCADE)
    cena = models.DecimalField(max_digits=5, decimal_places=2)
    obraz = models.TextField()
    kategoria = models.ForeignKey(Kategoria, on_delete=models.CASCADE)

class DaneUzytkownika(models.Model):
    imie = models.CharField(max_length=15)
    nazwisko = models.CharField(max_length=15)
    miejscowosc = models.CharField(max_length=20)
    ulica = models.CharField(max_length=60, null=True)
    nrDomu = models.CharField(max_length=6)
    nrMieszkania = models.CharField(max_length=6,null=True)
    telefon = models.IntegerField()
    email = models.EmailField()

class Zamowienia(models.Model):
    klient = models.ForeignKey(DaneUzytkownika, on_delete=models.CASCADE)
    
class PozycjaZamowienia(models.Model):
    zamowienie = models.ForeignKey(Zamowienia, on_delete=models.CASCADE)
    jedzenie = models.ForeignKey(Jedzenie, on_delete=models.CASCADE)
    ilosc = models.IntegerField()
    
'''class StanZamowienia(models.Model):  
    Skrot = models.CharField(max_length=1, primary_key = True)
    Stan = models.CharField(max_length=20)

class Zamowienia(models.Model):
    SkrotStan = models.ForeignKey(StanZamowienia, on_delete=models.CASCADE)
    
class PozycjaZamowienia(models.Model):
    IdZamowienia = models.ForeignKey(Zamowienia, on_delete=models.CASCADE)
    IdJedzenia = models.ForeignKey(Jedzenie, on_delete=models.CASCADE)
'''