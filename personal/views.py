from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'personal/home.html')


def contact(request):
    return render(request, 'personal/contact.html', {'content': ['If you want mail me, this is my email: ', '15_yurchik@ukr.net']})
