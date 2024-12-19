from django.shortcuts import render

# Create your views here.
def description(request):
    template_name = 'homepage/description.html'
    return render(request, template_name=template_name)