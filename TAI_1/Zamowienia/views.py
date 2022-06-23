from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render, redirect
from Zamowienia import models
import math
import json
from .requests import connect_post, connect_get, connect_put
from django.core.serializers.json import DjangoJSONEncoder
#from .forms import Platnosc
from django.views.decorators.csrf import csrf_exempt
from operator import itemgetter





zawartosc = {
        "tytul": "Strona Główna",
        "autor": "Mateusz Szmyt WCY19IJ3S1",
        "data_wydania": "2021-2022"
    }

def home(request):
    extID = 137
    if(request.GET.get("cleanAll")):
        request.session.flush()
        e = {"koszyk": 0, "lista": None}
        zawartosc.update(e)
        return render(request, "html/Strona_glowna.html", zawartosc)
        
    
    z = {
    "cart": request.GET.get("Cart"),
    "about": request.GET.get("About"),
    "restaurants": request.GET.get("Restaurants"),
    "menu": request.GET.get("Menu"),
    "contact": request.GET.get("Contact"),
    }
    zawartosc.update(z)
    
    if not 'koszyk' in request.session or not request.session['koszyk']:
        kosz = 0
        request.session.setdefault('koszyk', [])
    else:
        kosz = len(request.session['koszyk'])
        print(kosz)
    
    if request.method == 'POST':
        for i in range(1, models.Jedzenie.objects.last().id+1):
            if request.POST.get(str(i)):
                print(i)
                #dodawanie do sesji?
                #request.session.flush()
                request.session.modified = True
                request.session['koszyk'].append(i)
                request.session.modified = True
                print(request.session['koszyk'])
                break
    
    t = []
    
    dictory = {"Jedzenie": [], "Restauracje": []}
    #Uzupełnianie Jedzenia
    for n in models.Jedzenie.objects.all():
        t.append(n)#.Nazwa)
    my_iter_list = iter(t)
    
    t = []
    for i in range(0,math.ceil(models.Jedzenie.objects.last().id/3)):
        t.append([next(my_iter_list),next(my_iter_list),next(my_iter_list)])
    dictory["Jedzenie"].append(t)  

    t = []
    #Uzupełnianie restauracji
    for n in models.Restauracja.objects.all():
        t.append(n)#.Nazwa)
        
    dictory["Restauracje"].append(t)
      
    e = {"koszyk": kosz, "lista": request.session['koszyk']}  
    print("Em: "+str(kosz))
    zawartosc.update(e)
    zawartosc.update(dictory)
    return render(request, "html/Strona_glowna.html", zawartosc)

def sortowanie(request):
    a =  sorted(request.session["koszyk"], key=itemgetter('id_produktu'))
    request.session["koszyk"] = a
     
@csrf_exempt 
def endpoint_Restaurant(request):
    lista = []
    for i in models.Restauracja.objects.all():#Dodawanie elementów do listy
        t = {"pos_id":i.id, "nazwa":i.nazwa, "logo":i.logo}
        lista.append(t)
    data = {"content":lista}#Dodanie listy elementów do słownika Dict(Zmapowanie)
    if request.method == 'GET':
        return JsonResponse(data)
    elif request.method == 'POST':
        return HttpResponse("Jebło z POST'a")
    elif request.method == 'PUT':
        return HttpResponse("Jebło z PUT'a")
    elif request.method == 'DELETE':
        return HttpResponse("Jebło z DELETE'a")    
    
@csrf_exempt 
def endpoint_Food(request):
    lista = []
    for i in models.Jedzenie.objects.all():#Dodawanie elementów do listy
        t = {"pos_id":i.id, "Nazwa":i.nazwa, "Id_Restauracji":i.idRestauracji_id, "Cena":i.cena, "Kategoria":i.kategoria_id, "Obraz":i.obraz}
        lista.append(t)
    data = {"content":lista}#Dodanie listy elementów do słownika Dict(Zmapowanie)
    if request.method == 'GET':
        return JsonResponse(data)
    elif request.method == 'POST':
        return HttpResponse("Jebło z POST'a")
    elif request.method == 'PUT':
        return HttpResponse("Jebło z PUT'a")
    elif request.method == 'DELETE':
        return HttpResponse("Jebło z DELETE'a")

@csrf_exempt      
def apitest(request, id):
    data = {}
    for i in models.Jedzenie.objects.all():
        if(i.id==id):
            data = {"pos_id":i.id, "Nazwa":i.nazwa, "Id_Restauracji":i.idRestauracji_id, "Cena":i.cena, "Kategoria":i.kategoria_id, "Obraz":i.obraz}
    #models.Jedzenie.objects
    if request.method == 'GET':
        return JsonResponse(data)
    else:
        raise Http404("Polecenie nieobsługiwane przez nasz serwer")

@csrf_exempt  
def addtobucket(request, id):
    if request.method == 'POST':
        
        #Sprawdzenie, czy w sesji występuje już taki sam id, jeżeli tak to zmień liczbę wystąpień

        flaga_ilosc = 0
        for i in request.session['koszyk']:
            if id == i.get("id_produktu"):
                request.session.modified = True
                request.session["koszyk"].remove({"id_produktu":id, "ilosc":i.get("ilosc")})
                request.session["koszyk"].append({"id_produktu":id, "ilosc":i.get("ilosc")+1})
                flaga_ilosc = 1
                break
        if flaga_ilosc == 0:
            request.session.modified = True
            request.session['koszyk'].append({"id_produktu":id, "ilosc":1})
            
        sortowanie(request)    
        print(request.session['koszyk'])
        return redirect(menu)

        
def inputData(request):
    if not 'url' in request.session or not request.session['url']:
        return redirect(home)
    if request.method == 'POST':
        data = models.DaneUzytkownika()
        print("imie = "+request.POST.get('imie'))
        data.imie = request.POST.get('imie')
        data.nazwisko = request.POST.get('nazwisko')
        data.miejscowosc = request.POST.get('miejscowosc')
        data.ulica = request.POST.get('ulica')
        data.nrDpmu = request.POST.get('nrdomu')
        data.nrMieszkania = request.POST.get('nrmieszkania')
        data.telefon = request.POST.get('telefon')
        data.email = request.POST.get('email')
        data.save()
        
        order = models.Zamowienia()
        order.klient_id = models.DaneUzytkownika.objects.last().id
        order.save()
        
        for i in request.session['koszyk']:
            orderpos = models.PozycjaZamowienia()
            orderpos.jedzenie_id = i.get("id_produktu")
            orderpos.ilosc = i.get("ilosc")
            orderpos.zamowienie_id = models.Zamowienia.objects.last().id
            orderpos.save()
        del request.session["koszyk"]
        return redirect(request.session['url'])
        #przenieś na wymażoną stronę
    return render(request, "html/Dane.html")


def bucket(request):
    #jeżeli jest sesja z OrderId
    if request.method == 'POST':
        if request.POST.get("reset"):
            print(request.session["koszyk"])
            del request.session["koszyk"]
            #request.session.flush() #Kasuje wszystkie sesje
        elif request.POST.get("zamowienie"):
            print("Składam zamówienie")
            url = "https://secure.snd.payu.com/pl/standard/user/oauth/authorize"
            data={
                "grant_type": "client_credentials",
                "client_id": 435431,
                "client_secret": "21d834ea1ce3272d591e81d2bc226b8c",
                }
        
            polaczenie = connect_post(url, None, data, None)
        
        
            if polaczenie.status_code == 200:
                data = polaczenie.json()
                token = f"{data['token_type'].capitalize()} {data['access_token']}"
                print(token)
                
                cena = 0
                for i in request.session['koszyk']:
                
                    cena+= i.get("ilosc") * models.Jedzenie.objects.filter(id=i.get("id_produktu"))[0].cena
                print(cena)
                
                cena = int(cena*100) #mnożenie przez 100 aby pozbyć się groszy(normalizacja)
                print(cena)
                data1={
                    "continueUrl": "http://127.0.0.1:8000",
                    "customerIp": "127.0.0.1",#adres IP
                    "merchantPosId": 435431,
                    "description": "Zamówienie jedzenia z portalu OrderInOne",#Opis płatności
                    "currencyCode": "PLN",#Waluta
                    "totalAmount": cena, #Cena liczona w groszach
                    "name": "Total order",#Nazwa przelewu
                    "unitPrice": 200, 
                    "quantity": 1
                }
            
                enc = json.dumps(data1, cls=DjangoJSONEncoder)
            
                url = "https://secure.snd.payu.com/api/v2_1/orders"
                headers={"Authorization": token,
                    "Content-Type": "application/json",
                    }
            
                polaczenie2 = connect_post(url, headers, enc, False)
                print(polaczenie2)
                print(polaczenie2.json())
                if polaczenie2.status_code == 302:#kod 302 oznacza przekierowanie na inną stronę
                    print(polaczenie2.json())
                    #zmienna sesyjna dla OrderID
                    
                    request.session['OrderId'] = polaczenie2.json()['orderId']
                    
                    url = "https://secure.snd.payu.com/api/v2_1/orders/" + str(request.session['OrderId'])
                    
                    
                    headers = {"Authorization": token,
                    "Content-Type": "application/json",
                    }
                    
                    polaczenie3 = connect_get(url, headers)
                    print(polaczenie3.status_code)
                    print(polaczenie3.json())
                    print(polaczenie3.json()["orders"][0]["status"])
                    request.session['url'] = polaczenie2.json()['redirectUri']
                    return redirect(inputData)
                else:
                    print("Wystąpił błąd")
            else:
                print("Wystąpił błąd")

        else:
            for i in models.Jedzenie.objects.all():
                if request.POST.get(str(i.id)):
                    for j in request.session["koszyk"]:
                        if j.get("id_produktu")==i.id:
                    #usuwanie z koszyka.
                            if j.get("ilosc")>1:
                                request.session.modified = True
                                request.session["koszyk"].remove({"id_produktu":i.id, "ilosc":j.get("ilosc")})
                                request.session["koszyk"].append({"id_produktu":i.id, "ilosc":j.get("ilosc")-1})
                            else:
                                request.session.modified = True
                                request.session["koszyk"].remove({"id_produktu":i.id, "ilosc":j.get("ilosc")})
                            break
    #posortować sesję względem id
            sortowanie(request)
    
    return render(request, "html/Koszyk.html")
    
def about(request):
    return render(request, "html/About.html")
    
def restaurants(request):
    return render(request, "html/Restauracje.html")
    
def menu(request):
    if not 'koszyk' in request.session or not request.session['koszyk']:
        request.session.setdefault('koszyk', [])
    
    return render(request, "html/Menu.html")
    
def contact(request):
    return render(request, "html/Kontakt.html")