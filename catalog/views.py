from django.shortcuts import HttpResponse

# Create your views here.
def view_catalog(request):
    return HttpResponse('Страница со списком товаров') 