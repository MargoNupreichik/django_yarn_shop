from django.shortcuts import render


# Create your views here.
def description(request):
    template_name = 'homepage/main.html'
    return render(request, template_name=template_name)
