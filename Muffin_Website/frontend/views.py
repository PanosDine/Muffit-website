from django.shortcuts import render

# Create your views here.
def index(request, *args, **kwargs):
    return render(request, 'frontend/index.html')


"""def contact(request):
    return render(request, 'frontend/contact.html')


def createOrder(request):
    return render(request, 'frontend/index.html')"""