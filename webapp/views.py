from django.http import HttpResponse


def index(request):
    return HttpResponse('<h2>HEY!</h2>')
