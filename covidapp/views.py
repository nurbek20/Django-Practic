from django.shortcuts import render
import requests
from django.http import HttpResponseRedirect
from covidapp.models import Contact

# Create your views here.
def main(request):
    return render(request, "index.html")


def covid(request):
    return render(request, "covid.html")


def search(request):
    if request.method == "POST":
        country = request.POST.get("country")
        covid_API = f"https://covid-api.mmediagroup.fr/v1/cases?country={country}"
        res = requests.get(covid_API)
        data = res.json()
        confirmed = data["All"]["confirmed"]
        country1=data['All']['country']
        deaths=data['All']['deaths']
        population=data['All']['population']
        
        return render(request,  'covid.html', {'data' :data, 'covid' :covid, 'deaths' :deaths, 'country1' :country1, 'population' :population, })


def message(request):
    if request.method=='POST':
        send=Contact()
        send.last_name=request.POST.get('last_name')
        send.first_name=request.POST.get("first_name")
        send.email=request.POST.get('email')
        send.number=request.POST.get('number')
        send.save()
        return HttpResponseRedirect('/')
