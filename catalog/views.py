from django.shortcuts import render


# Create your views here.
def view_catalog(request):
    template_name = 'catalog/catalog.html'
    return render(request, template_name=template_name)
