import requests
from django.shortcuts import render


from bs4 import BeautifulSoup


BASE_CRAIGSLIST_URL = 'https://kerala.craigslist.org/search/bbb?query={}'
# Create your views here.
def home(request):
    return render(request, 'base.html')

def new_search(request):
    search = request.POST.get('search')
    response = requests.get('https://kerala.craigslist.org/search/bbb?query=bus&sort=rel')
    data = response.text
    print(data)
    stuff_for_frontend = {'search':search}
    return render(request,  'my_app/new_search.html',stuff_for_frontend)