from django.shortcuts import render


# Create your views here.
def create_order(request):
    template_name = 'order/order_info.html'
    return render(request, template_name=template_name)
