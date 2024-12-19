from django.shortcuts import HttpResponse

# Create your views here.
def view_contacts(request):
    return HttpResponse('Здесь будет находится контактная информация.')