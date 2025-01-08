from django.shortcuts import render


# Create your views here.
def view_contacts(request):
    template_name = 'contact/contact_info.html'
    return render(request, template_name=template_name)
