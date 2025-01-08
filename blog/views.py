from django.shortcuts import render


# Create your views here.
def news_feed(request):
    template_name = 'blog/blog.html'
    return render(request, template_name=template_name)
