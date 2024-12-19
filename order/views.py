from django.shortcuts import HttpResponse

# Create your views here.
def create_order(request):
    return HttpResponse('Здесь пользователь сможет оформитьь заказ.')