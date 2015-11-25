from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
    template = loader.get_template('healthDirectory/register.html')