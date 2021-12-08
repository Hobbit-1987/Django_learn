from django.http import HttpResponse

def hallo(request):
    return HttpResponse ('<h1>hallo</h1>')
