from django.shortcuts import render


from .models import CarouselImage

# Create your views here.
def homeView(request):
    template = 'mainapp/home.html'
    context = {

        'current_page' : 'home',

        'carousel_images' : CarouselImage.objects.all()
            }

    return render(request, template_name=template, context=context)

    
def aboutView(request):
    template = 'mainapp/about.html'
    context = {}

    return render(request, template_name=template, context=context)

    
def contactView(request):
    template = 'mainapp/contact.html'
    context = {}

    return render(request, template_name=template, context=context)

    
    